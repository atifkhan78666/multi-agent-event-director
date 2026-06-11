from graph import app


event = input(
    "Describe your event: "
)
result = app.invoke(
    {
        "event_details": event
    })


print("\n")
print(result["final_report"])

