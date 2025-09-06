from datetime import datetime

from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext


# def get_current_time() -> dict:
#     """Get the current time in the format YYYY-MM-DD HH:MM:SS"""
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#     }


# def refund_course(tool_context: ToolContext) -> dict:
#     """
#     Simulates refunding the AI Marketing Platform course.
#     Updates state by removing the course from purchased_courses.
#     """
#     course_id = "ai_marketing_platform"
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     # Get current purchased courses
#     current_purchased_courses = tool_context.state.get("purchased_courses", [])

#     # Check if user owns the course
#     course_ids = [
#         course["id"] for course in current_purchased_courses if isinstance(course, dict)
#     ]
#     if course_id not in course_ids:
#         return {
#             "status": "error",
#             "message": "You don't own this course, so it can't be refunded.",
#         }

#     # Create new list without the course to be refunded
#     new_purchased_courses = []
#     for course in current_purchased_courses:
#         # Skip empty entries or non-dict entries
#         if not course or not isinstance(course, dict):
#             continue
#         # Skip the course being refunded
#         if course.get("id") == course_id:
#             continue
#         # Keep all other courses
#         new_purchased_courses.append(course)

#     # Update purchased courses in state via assignment
#     tool_context.state["purchased_courses"] = new_purchased_courses

#     # Get current interaction history
#     current_interaction_history = tool_context.state.get("interaction_history", [])

#     # Create new interaction history with refund added
#     new_interaction_history = current_interaction_history.copy()
#     new_interaction_history.append(
#         {"action": "refund_course", "course_id": course_id, "timestamp": current_time}
#     )

#     # Update interaction history in state via assignment
#     tool_context.state["interaction_history"] = new_interaction_history

#     return {
#         "status": "success",
#         "message": """Successfully refunded the AI Marketing Platform course! 
#          Your $149 will be returned to your original payment method within 3-5 business days.""",
#         "course_id": course_id,
#         "timestamp": current_time,
#     }


# Create the trade execution agent
trade_execution_agent = Agent(
    name="trade_execution_agent",
    model="gemini-2.0-flash",
    description="Order agent for viewing purchase history and processing refunds",
    instruction="""
    You are the portfolio agent for the Stock & Investing Assistant platform.
    Your role is to help users view, summarize, and manage their investment portfolio and transaction history.

    <user_info>
    Name: {user_name}
    </user_info>

    <portfolio_info>
    Portfolio: {portfolio}
    </portfolio_info>

    <interaction_history>
    {interaction_history}
    </interaction_history>

    When users ask about their portfolio:
    1. Check their portfolio above for current holdings
       - Each asset is stored as an object with "ticker", "shares", "purchase_date", and "purchase_price" properties
    2. Format the response clearly showing:
       - Which assets they own
       - How many shares of each
       - When and at what price they were purchased

    When users ask about performance or allocation:
    1. Summarize portfolio value and diversification
    2. Highlight gains/losses if data is available

    When users request to remove or update an asset:
    1. Verify they own the asset (check ticker in portfolio)
    2. If they own it:
       - Update or remove the asset as requested
       - Confirm the change and summarize the updated portfolio
    3. If they don't own it:
       - Inform them they don't own the asset

    Example Response for Portfolio Summary:
    "Here is your current portfolio:
    1. AAPL - 10 shares @ $180.50 (purchased on: 2025-09-01)
    2. TSLA - 5 shares @ $250.00 (purchased on: 2025-08-15)"

    If they haven't invested yet:
    - Let them know their portfolio is empty
    - Suggest talking to the market info agent for ideas or the trade execution agent to start investing

    Remember:
    - Be clear and professional
    - Summarize holdings and performance accurately
    - Direct market questions to market info agent
    - Direct trade requests to trade execution agent
    """,
    tools=[],
)
