#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ParkingGoodsDetail(object):

    def __init__(self):
        self._arg_date_week = None
        self._arg_end_time = None
        self._arg_start_time = None
        self._biz_data = None
        self._buy_end_date = None
        self._buy_start_date = None
        self._cost_price = None
        self._count_num = None
        self._current_price = None
        self._date_num = None
        self._desc = None
        self._end_sell_time = None
        self._goods_id = None
        self._goods_num = None
        self._goods_rent_type = None
        self._goods_status = None
        self._goods_type = None
        self._keywords = None
        self._name = None
        self._out_id = None
        self._parking_id = None
        self._put_time = None
        self._start_sell_time = None

    @property
    def arg_date_week(self):
        return self._arg_date_week

    @arg_date_week.setter
    def arg_date_week(self, value):
        self._arg_date_week = value
    @property
    def arg_end_time(self):
        return self._arg_end_time

    @arg_end_time.setter
    def arg_end_time(self, value):
        self._arg_end_time = value
    @property
    def arg_start_time(self):
        return self._arg_start_time

    @arg_start_time.setter
    def arg_start_time(self, value):
        self._arg_start_time = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def buy_end_date(self):
        return self._buy_end_date

    @buy_end_date.setter
    def buy_end_date(self, value):
        self._buy_end_date = value
    @property
    def buy_start_date(self):
        return self._buy_start_date

    @buy_start_date.setter
    def buy_start_date(self, value):
        self._buy_start_date = value
    @property
    def cost_price(self):
        return self._cost_price

    @cost_price.setter
    def cost_price(self, value):
        self._cost_price = value
    @property
    def count_num(self):
        return self._count_num

    @count_num.setter
    def count_num(self, value):
        self._count_num = value
    @property
    def current_price(self):
        return self._current_price

    @current_price.setter
    def current_price(self, value):
        self._current_price = value
    @property
    def date_num(self):
        return self._date_num

    @date_num.setter
    def date_num(self, value):
        self._date_num = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def end_sell_time(self):
        return self._end_sell_time

    @end_sell_time.setter
    def end_sell_time(self, value):
        self._end_sell_time = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_num(self):
        return self._goods_num

    @goods_num.setter
    def goods_num(self, value):
        self._goods_num = value
    @property
    def goods_rent_type(self):
        return self._goods_rent_type

    @goods_rent_type.setter
    def goods_rent_type(self, value):
        self._goods_rent_type = value
    @property
    def goods_status(self):
        return self._goods_status

    @goods_status.setter
    def goods_status(self, value):
        self._goods_status = value
    @property
    def goods_type(self):
        return self._goods_type

    @goods_type.setter
    def goods_type(self, value):
        self._goods_type = value
    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        self._keywords = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value
    @property
    def put_time(self):
        return self._put_time

    @put_time.setter
    def put_time(self, value):
        self._put_time = value
    @property
    def start_sell_time(self):
        return self._start_sell_time

    @start_sell_time.setter
    def start_sell_time(self, value):
        self._start_sell_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.arg_date_week:
            if hasattr(self.arg_date_week, 'to_alipay_dict'):
                params['arg_date_week'] = self.arg_date_week.to_alipay_dict()
            else:
                params['arg_date_week'] = self.arg_date_week
        if self.arg_end_time:
            if hasattr(self.arg_end_time, 'to_alipay_dict'):
                params['arg_end_time'] = self.arg_end_time.to_alipay_dict()
            else:
                params['arg_end_time'] = self.arg_end_time
        if self.arg_start_time:
            if hasattr(self.arg_start_time, 'to_alipay_dict'):
                params['arg_start_time'] = self.arg_start_time.to_alipay_dict()
            else:
                params['arg_start_time'] = self.arg_start_time
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.buy_end_date:
            if hasattr(self.buy_end_date, 'to_alipay_dict'):
                params['buy_end_date'] = self.buy_end_date.to_alipay_dict()
            else:
                params['buy_end_date'] = self.buy_end_date
        if self.buy_start_date:
            if hasattr(self.buy_start_date, 'to_alipay_dict'):
                params['buy_start_date'] = self.buy_start_date.to_alipay_dict()
            else:
                params['buy_start_date'] = self.buy_start_date
        if self.cost_price:
            if hasattr(self.cost_price, 'to_alipay_dict'):
                params['cost_price'] = self.cost_price.to_alipay_dict()
            else:
                params['cost_price'] = self.cost_price
        if self.count_num:
            if hasattr(self.count_num, 'to_alipay_dict'):
                params['count_num'] = self.count_num.to_alipay_dict()
            else:
                params['count_num'] = self.count_num
        if self.current_price:
            if hasattr(self.current_price, 'to_alipay_dict'):
                params['current_price'] = self.current_price.to_alipay_dict()
            else:
                params['current_price'] = self.current_price
        if self.date_num:
            if hasattr(self.date_num, 'to_alipay_dict'):
                params['date_num'] = self.date_num.to_alipay_dict()
            else:
                params['date_num'] = self.date_num
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.end_sell_time:
            if hasattr(self.end_sell_time, 'to_alipay_dict'):
                params['end_sell_time'] = self.end_sell_time.to_alipay_dict()
            else:
                params['end_sell_time'] = self.end_sell_time
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_num:
            if hasattr(self.goods_num, 'to_alipay_dict'):
                params['goods_num'] = self.goods_num.to_alipay_dict()
            else:
                params['goods_num'] = self.goods_num
        if self.goods_rent_type:
            if hasattr(self.goods_rent_type, 'to_alipay_dict'):
                params['goods_rent_type'] = self.goods_rent_type.to_alipay_dict()
            else:
                params['goods_rent_type'] = self.goods_rent_type
        if self.goods_status:
            if hasattr(self.goods_status, 'to_alipay_dict'):
                params['goods_status'] = self.goods_status.to_alipay_dict()
            else:
                params['goods_status'] = self.goods_status
        if self.goods_type:
            if hasattr(self.goods_type, 'to_alipay_dict'):
                params['goods_type'] = self.goods_type.to_alipay_dict()
            else:
                params['goods_type'] = self.goods_type
        if self.keywords:
            if hasattr(self.keywords, 'to_alipay_dict'):
                params['keywords'] = self.keywords.to_alipay_dict()
            else:
                params['keywords'] = self.keywords
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_id:
            if hasattr(self.out_id, 'to_alipay_dict'):
                params['out_id'] = self.out_id.to_alipay_dict()
            else:
                params['out_id'] = self.out_id
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        if self.put_time:
            if hasattr(self.put_time, 'to_alipay_dict'):
                params['put_time'] = self.put_time.to_alipay_dict()
            else:
                params['put_time'] = self.put_time
        if self.start_sell_time:
            if hasattr(self.start_sell_time, 'to_alipay_dict'):
                params['start_sell_time'] = self.start_sell_time.to_alipay_dict()
            else:
                params['start_sell_time'] = self.start_sell_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ParkingGoodsDetail()
        if 'arg_date_week' in d:
            o.arg_date_week = d['arg_date_week']
        if 'arg_end_time' in d:
            o.arg_end_time = d['arg_end_time']
        if 'arg_start_time' in d:
            o.arg_start_time = d['arg_start_time']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'buy_end_date' in d:
            o.buy_end_date = d['buy_end_date']
        if 'buy_start_date' in d:
            o.buy_start_date = d['buy_start_date']
        if 'cost_price' in d:
            o.cost_price = d['cost_price']
        if 'count_num' in d:
            o.count_num = d['count_num']
        if 'current_price' in d:
            o.current_price = d['current_price']
        if 'date_num' in d:
            o.date_num = d['date_num']
        if 'desc' in d:
            o.desc = d['desc']
        if 'end_sell_time' in d:
            o.end_sell_time = d['end_sell_time']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_num' in d:
            o.goods_num = d['goods_num']
        if 'goods_rent_type' in d:
            o.goods_rent_type = d['goods_rent_type']
        if 'goods_status' in d:
            o.goods_status = d['goods_status']
        if 'goods_type' in d:
            o.goods_type = d['goods_type']
        if 'keywords' in d:
            o.keywords = d['keywords']
        if 'name' in d:
            o.name = d['name']
        if 'out_id' in d:
            o.out_id = d['out_id']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'put_time' in d:
            o.put_time = d['put_time']
        if 'start_sell_time' in d:
            o.start_sell_time = d['start_sell_time']
        return o


