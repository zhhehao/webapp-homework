#!/usr/bin/env python
# -*- coding: utf-8 -*-

'This is a orm for web app'

__author__ = 'Bruce He'

import logging
logging.basicConfig(level=logging.INFO)

import asyncio

async def create_pool(loop, **kw):
	logging.info('create database connection pool...')
	global __pool
	__pool = await aiomysql.create_pool(
		host=kw.get('host', 'localhost'),
		port=kw.get('port', '3306'),
		user=kw.['user'],
		password=kw.['password'],
		db=kw['db'],
		charset=kw.get('charset', 'utf-8'),
		autocommit=kw.get('autocommit', True),
		maxsize=kw.get('maxsize', 10),
		minsize=kw.get('minsize', 1),
		loop=loop
	)
