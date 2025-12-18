from app.pro.evolution.watcher.news import fetch_public_news
from app.pro.evolution.analyzer.events import extract_structuring_events
from app.pro.evolution.analyzer.trajectories import build_trajectory
from app.pro.evolution.curator.rules import validate_case
from app.pro.evolution.updater.case_store import add_case

def run_evolution_cycle():
	articles = fetch_public_news()

	for a in articles:
		events = extract_structuring_events(a["content"])

		if not events:
			continue

		case = build_trajectory(
			events=events,
			context={}
		)

		if validate_case(case):
			add_case(case)
# Module: scheduler.py
# Orchestration des tâches de veille, extraction, validation et mise à jour
