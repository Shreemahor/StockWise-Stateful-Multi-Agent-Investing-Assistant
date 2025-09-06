from datetime import datetime

from google.adk.agents import Agent
#from google.adk.tools import google_search
from google.adk.tools import google_search

# def purchase_course(tool_context: ToolContext) -> dict:
#     """
#     Simulates purchasing the AI Marketing Platform course.
#     Updates state with purchase information.
#     """
#     course_id = "ai_marketing_platform"
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     # Get current purchased courses
#     current_purchased_courses = tool_context.state.get("purchased_courses", [])

#     # Check if user already owns the course
#     course_ids = [
#         course["id"] for course in current_purchased_courses if isinstance(course, dict)
#     ]
#     if course_id in course_ids:
#         return {"status": "error", "message": "You already own this course!"}

#     # Create new list with the course added
#     new_purchased_courses = []
#     # Only include valid dictionary courses
#     for course in current_purchased_courses:
#         if isinstance(course, dict) and "id" in course:
#             new_purchased_courses.append(course)

#     # Add the new course as a dictionary with id and purchase_date
#     new_purchased_courses.append({"id": course_id, "purchase_date": current_time})

#     # Update purchased courses in state via assignment
#     tool_context.state["purchased_courses"] = new_purchased_courses

#     # Get current interaction history
#     current_interaction_history = tool_context.state.get("interaction_history", [])

#     # Create new interaction history with purchase added
#     new_interaction_history = current_interaction_history.copy()
#     new_interaction_history.append(
#         {"action": "purchase_course", "course_id": course_id, "timestamp": current_time}
#     )

#     # Update interaction history in state via assignment
#     tool_context.state["interaction_history"] = new_interaction_history

#     return {
#         "status": "success",
#         "message": "Successfully purchased the AI Marketing Platform course!",
#         "course_id": course_id,
#         "timestamp": current_time,
#     }


# Create the market info agent
market_info_agent = Agent(
    name="market_info_agent",
    model="gemini-2.0-flash",
    description="Market information agent",
    instruction="""
    You are the market information agent for the Stock & Investing Assistant platform. Your role is to provide users with real-time stock market data, financial news, and market trends.

    <user_info>
    Name: {user_name}
    </user_info>

    <portfolio_info>
    Portfolio: {portfolio}
    </portfolio_info>

    <interaction_history>
    {interaction_history}
    </interaction_history>

    Market Info Capabilities:
    - Provide current stock prices, indices, and market movements
    - Share financial news and analysis relevant to the user's interests
    - Use general knowledge to find up-to-date information and news

    When interacting with users:
    1. If the user asks about a specific stock or market trend:
       - Use google_search to retrieve the latest data and news
       - Summarize key points and trends
    2. If the user asks about their portfolio assets:
       - Reference the portfolio above to provide personalized insights
    3. For general market questions:
       - Offer broad market summaries and highlight notable events

    After any interaction:
    - The state will automatically track the interaction
    - Be ready to hand off to other agents for portfolio management or trade execution as needed

    Remember:
    - Be accurate and concise
    - Focus on actionable insights and relevant news
    - Use general knowledge to ensure information is current
    """,
    tools=[],
)
