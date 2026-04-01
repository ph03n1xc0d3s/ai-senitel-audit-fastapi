import httpx 

async def analyze_code_security(code: str) -> dict: 
    # Call to an external security analysis API could be made here, but for simplicity, we will mock the response.
    # Using async with httpx for keeping concurrency smooth
    async with httpx.AsyncClient() as client:
        # Mock logic: checking for 'eval' or 'password' as a simple example
        findings = []
        if "eval(" in code:
            findings.append("Use of eval() can lead to code injection vulnerabilities.")
        if "exec(" in code:
            findings.append("Use of exec() can lead to code injection vulnerabilities.")
        if "password =" in code:
            findings.append("Hardcoded passwords can lead to security risks.") 

        score = 10.0 if not findings else max(10.0 - (len(findings) * 3))
        return {
            "findings": findings,
            "score": max(0, score)
        }