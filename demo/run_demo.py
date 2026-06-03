from agent_forge import AgentRuntime

if __name__ == "__main__":
    runtime = AgentRuntime()
    outcome = runtime.run("Prepare a customer churn action plan", amount_usd=25000)
    print("Results:")
    for item in outcome["results"]:
        print("-", item)
    print("Policy:", outcome["policy"])
    print("Audit trail:")
    for line in outcome["audit_log"]:
        print("-", line)