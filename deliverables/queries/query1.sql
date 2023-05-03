/*
Query 1:
*/
select Distinct TO_CHAR(A.created_time,'YYYY-MM-DD'), sum(A.comment_count) as comment_count
FROM (select Distinct created_time, h_id, post_h_id, comment_h_id, max(comment_count) as comment_count
	  from commentdata.comment_info
	  group by created_time, h_id, post_h_id, comment_h_id) A
group by TO_CHAR(A.created_time,'YYYY-MM-DD')
order by sum(A.comment_count) desc



select *
FROM commentdata.comment_info;