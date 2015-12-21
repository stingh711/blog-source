Title: Postgresql is great
Date: 2015-07-02 13:43:43
Tags: postgresql
Category: postgresql
Slug: postgresql-is-great
Author: Sting
Summary: Postgres is so great.


Target: study postgresql's feature and how to use them effective on PDMS' dynamic form's save and search.

Table schema is as following:

    id         | integer           | not null default nextval('data_id_seq'::regclass) | plain    |              |
    patient_id | integer           |                                                   | plain    |              |
    item_id    | integer           |                                                   | plain    |              |
    data_type  | integer           |                                                   | plain    |              |
    value      | character varying |
    `</pre>

Column value is used to save the value of dynamic form which has 5 types. They are string, integer, float, date and options. I use varchar here and want to convert it to the actual data type when doing query.

I added other three partial indexes base on different data types. Thanks to postgresql's partial index.

"data_value_dict_index" btree ((value::integer)) WHERE data_type = 3
"data_value_integer_index" btree ((value::integer)) WHERE data_type = 2
"data_value_text_index" btree (value) WHERE data_type = 1

Then I inserted about 10000000 records into the table and run following SQL.

    select distinct patient_id from data where data_type = 2 and item_id = 2 and value::int > 500 limit 20;
    => 2.2s
    (select distinct patient_id from data where data_type = 2 and item_id = 2 and value::int > 700) intersect (select patient_id from data where data_type = 1 and item_id = 9 and value = '99');
    => 2.0s

The result is not bad. More importantly, postgresql has intersect which is very useful for PDMS. Its partial index is also great. Although I save value as string and convert it to other type in query, the indexes still work.

Then I adjusted the indexed by adding item_id column, the result turned out to be amazing.

    select distinct patient_id from data where data_type = 2 and item_id = 2 and value::int > 500 limit 20
    => 118.640 ms
    (select distinct patient_id from data where data_type = 2 and item_id = 2 and value::int > 700) intersect (select patient_id from data where data_type = 1 and item_id = 9 and value = '99')
    => 143 ms

The indexes is now:

    "data_value_dict_index" btree (item_id, (value::integer)) WHERE data_type = 3
    "data_value_integer_index" btree (item_id, (value::integer)) WHERE data_type = 2
    "data_value_text_index" btree (item_id, value) WHERE data_type = 1
    
