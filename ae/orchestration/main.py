import asyncio

from ae.core.system_orchestrator import SystemOrchestrator

if __name__ == "__main__":
    orchestrator = SystemOrchestrator(agent_scenario="user_proxy,browser_nav_agent",input_mode="GUI_ONLY", orchestrater_mode=True)
    asyncio.run(orchestrator.start())
