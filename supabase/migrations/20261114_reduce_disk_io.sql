-- 14/11/2026 : alerte Supabase « Disk IO Budget ». Robot de prospection ralenti (crawl 20 s → 5 min, search 2 → 15 min,
-- nouveaux 5 → 30 min), alerte leads 1 → 2 min, purge quotidienne de cron.job_run_details (garde 2 jours). Appliquée via MCP.
select cron.alter_job((select jobid from cron.job where jobname='clicandsite-crawl'), schedule := '*/5 * * * *');
select cron.alter_job((select jobid from cron.job where jobname='clicandsite-search'), schedule := '*/15 * * * *');
select cron.alter_job((select jobid from cron.job where jobname='clicandsite-nouveaux'), schedule := '*/30 * * * *');
select cron.alter_job((select jobid from cron.job where jobname='cs-lead-notify'), schedule := '*/2 * * * *');
delete from cron.job_run_details where end_time < now() - interval '2 days';
select cron.schedule('cs-cron-purge', '41 4 * * *', $$delete from cron.job_run_details where end_time < now() - interval '2 days'$$);
