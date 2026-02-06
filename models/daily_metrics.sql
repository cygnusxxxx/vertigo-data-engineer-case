with source_data as (

    select
        event_date,
        country,
        platform,
        user_id,
        match_start_count,
        match_end_count,
        victory_count,
        defeat_count,
        server_connection_error,
        iap_revenue,
        ad_revenue
    from {{ source('raw', 'user_daily_metrics') }}

)

select
    event_date,
    country,
    platform,

    count(distinct user_id) as dau,

    sum(iap_revenue) as total_iap_revenue,
    sum(ad_revenue) as total_ad_revenue,

    safe_divide(
        sum(iap_revenue) + sum(ad_revenue),
        count(distinct user_id)
    ) as arpdau,

    sum(match_start_count) as matches_started,

    safe_divide(
        sum(match_start_count),
        count(distinct user_id)
    ) as match_per_dau,

    safe_divide(
        sum(victory_count),
        nullif(sum(match_end_count), 0)
    ) as win_ratio,

    safe_divide(
        sum(defeat_count),
        nullif(sum(match_end_count), 0)
    ) as defeat_ratio,

    safe_divide(
        sum(server_connection_error),
        count(distinct user_id)
    ) as server_error_per_dau

from source_data
group by
    event_date, country, platform
