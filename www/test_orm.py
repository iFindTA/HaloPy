#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#


import orm, asyncio
from models import User, Blog, Comment

async def test(loop):
	await orm.create_pool(loop,user='www-data', password='www-data', db='awesome')

	u = User(name='nanhu', email='nanhujiaju@gmail.com', password='1234567890', image='about:blank')

	await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([test(loop)]))
loop.run_forever()