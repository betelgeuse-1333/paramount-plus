/*
Query 1: Which day had the highest number of top level comments (excluding replies)? 

Answer: date:2018-01-09 comment_count: 656
*/
select Distinct TO_CHAR(A.created_time,'YYYY-MM-DD'), sum(A.comment_count) as comment_count
FROM (select Distinct created_time, h_id, post_h_id, comment_h_id, max(comment_count) as comment_count
	  from commentdata.comment_info
	  group by created_time, h_id, post_h_id, comment_h_id) A
group by TO_CHAR(A.created_time,'YYYY-MM-DD')
order by sum(A.comment_count) desc



select *
FROM commentdata.comment_info;
