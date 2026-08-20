from src.agents.router import (
    get_router,
    classify_question
)

router = get_router()

while True:

    question = input("\nQuestion: ")

    route = classify_question(
        question,
        router
    )

    print("\nDecision:", route)