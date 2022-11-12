CREATE DATABASE Hostel_Management_System;
USE Hostel_Management_System;
CREATE TABLE hostel_xyz(num_rooms int(3),num_students int(4),annual_expense int(8));
CREATE TABLE Student(student_id varchar(8),name varchar(20),parents_name varchar(20),department varchar(20),age int(3),DOB date,yr varchar(2),PRIMARY KEY(student_id));
CREATE TABLE Room(room_id varchar(4) PRIMARY KEY,capacity int(2),yr varchar(2));
CREATE TABLE canteen(student_id varchar(8),item varchar(255),charge int(5));
CREATE TABLE visitor(visitor_name varchar(20),check_in time,room_id varchar(4),student_id varchar(8));