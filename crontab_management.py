from crontab import CronTab
import logger as log


def schedule_file_sync_cron_job(parsed_args) -> None:
    """Setup a cron daemon to repeatedly sync select folders."""
    if parsed_args.interval is not None:
        log.logger.info("Initializing file_sync cron job")
        job = (
            f"""*/{parsed_args.interval} * * * * python3 main.py """
            f"""{parsed_args.backup} {parsed_args.source} {parsed_args.log_path}"""
        )
        mem_cron = CronTab(tab=job)

        for _ in mem_cron.run_scheduler():  # Cron daemon.
            log.logger.debug(f"Cron: RUNNING {job}")
