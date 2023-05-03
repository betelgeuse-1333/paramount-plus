/*
Query 2:  Report back the number of comments, and comment up_likes, per type, for all
comments (top level and replies) made ​after​ 2018-01-10

*/


select Distinct type,
sum(ci.comment_count) as comment_count,
sum(ci.comment_count) as uplike_count
FROM (select Distinct created_time,
	  h_id,
	  post_h_id,
	  comment_h_id,
	  max(comment_count) as comment_count,
	  max(up_likes) as up_likes
	  from commentdata.comment_info
	  where created_time > '2018-01-10'
	  group by created_time, h_id, post_h_id, comment_h_id) ci
INNER JOIN commentdata.post_meta pm
on ci.post_h_id = pm.post_h_id
group by type
order by type

