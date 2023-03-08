1.SELECT "posts_text_post"."id", "posts_text_post"."user_id", "posts_text_post"."body", "posts_text_post"."created_at", "posts_text_post"."updated_at" FROM "posts_text_post"
 INNER JOIN "auth_user" ON ("posts_text_post"."user_id" = "auth_user"."id") 
 INNER JOIN "posts_posts_profile" ON ("auth_user"."id" = "posts_posts_profile"."user_id")
  WHERE "posts_posts_profile"."id" IN (SELECT U0."id" FROM "posts_posts_profile" U0 
  INNER JOIN "posts_posts_profile_follows" U1 ON (U0."id" = U1."to_posts_profile_id") 
  WHERE U1."from_posts_profile_id" = 23) ORDER BY "posts_text_post"."updated_at" DESC; args=(23,); 


2. SELECT "posts_posts_profile"."id", "posts_posts_profile"."user_id" FROM "posts_posts_profile" WHERE NOT ("posts_posts_profile"."user_id" = 23);

3.SELECT "cal_event"."id", "cal_event"."title", "cal_event"."priority", "cal_event"."description", "cal_event"."start_time", "cal_event"."end_time", "cal_event"."username_id" FROM "cal_event" 
WHERE (django_datetime_extract('month', "cal_event"."start_time", 'UTC', 'UTC') = 3 AND "cal_event"."start_time" BETWEEN '2023-01-01 00:00:00' AND '2023-12-31 23:59:59.999999' AND "cal_event"."username_id" = 23 
AND (django_datetime_extract('day', "cal_event"."start_time", 'UTC', 'UTC') >= 8
 OR django_datetime_extract('day', "cal_event"."end_time", 'UTC', 'UTC') >= 8)); 
 args=('month', 'UTC', 'UTC', 3, '2023-01-01 00:00:00', '2023-12-31 23:59:59.999999', 23, 'day', 'UTC', 'UTC', 8, 'day', 'UTC', 'UTC',8);

 4.SELECT "academic_subjects"."id", "academic_subjects"."subject_name" FROM "academic_subjects" WHERE "academic_subjects"."id" = 1 LIMIT 21; args=(1,);

 5. INSERT INTO "academic_tests" ("test_subject_id", "test_title", "test_given_date", "test_marks", "test_outof", "submitted", "username_id") VALUES (1, 'test', '2023-03-07 20:20:00', '10', '100', '2023-03-08', 23) RETURNING "academic_tests"."id"; args=(1, 'test', '2023-03-07 20:20:00', '10', '100', '2023-03-08', 23);

 6.UPDATE "academic_tests" SET "test_subject_id" = 1, "test_title" = 'changetitle', "test_given_date" = '2023-03-07 20:20:00', "test_marks" = '10', "test_outof" = '100', "submitted" = '2023-03-08', "username_id" = 23 WHERE "academic_tests"."id" = 20; args=(1, 'changetitle', '2023-03-07 20:20:00', '10', '100', '2023-03-08', 23, 20);

 7.INSERT INTO "posts_text_post" ("user_id", "body", "created_at", "updated_at") VALUES (23, 'hi', '2023-03-08 14:53:32.175935', '2023-03-08 14:53:32.175935') RETURNING "posts_text_post"."id"; args=(23, 'hi', '2023-03-08 14:53:32.175935', '2023-03-08 14:53:32.175935');