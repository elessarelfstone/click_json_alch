#!/bin/bash
set -e
clickhouse client -n <<-EOSQL
set allow_experimental_object_type = 1;
CREATE TABLE raw_json_test (data JSON, created_at DateTime DEFAULT now()) ENGINE = MergeTree() PARTITION BY toYYYYMM(created_at) ORDER BY created_at;
EOSQL