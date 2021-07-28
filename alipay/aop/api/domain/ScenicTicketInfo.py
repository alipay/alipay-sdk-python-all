#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenicExtInfo import ScenicExtInfo


class ScenicTicketInfo(object):

    def __init__(self):
        self._auto_check_time = None
        self._check_time = None
        self._close_time = None
        self._enter_way = None
        self._ext_info = None
        self._invalid_dates = None
        self._invalid_day_in_week = None
        self._picture = None
        self._price = None
        self._status = None
        self._ticket_count = None
        self._ticket_goods_id = None
        self._ticket_link = None
        self._ticket_name = None
        self._ticket_no = None
        self._ticket_specs = None
        self._ticket_type = None
        self._ticket_use_code = None
        self._ticket_use_pic = None
        self._use_end_date = None
        self._use_end_time = None
        self._use_start_date = None
        self._use_start_time = None

    @property
    def auto_check_time(self):
        return self._auto_check_time

    @auto_check_time.setter
    def auto_check_time(self, value):
        self._auto_check_time = value
    @property
    def check_time(self):
        return self._check_time

    @check_time.setter
    def check_time(self, value):
        self._check_time = value
    @property
    def close_time(self):
        return self._close_time

    @close_time.setter
    def close_time(self, value):
        self._close_time = value
    @property
    def enter_way(self):
        return self._enter_way

    @enter_way.setter
    def enter_way(self, value):
        self._enter_way = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ScenicExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ScenicExtInfo.from_alipay_dict(i))
    @property
    def invalid_dates(self):
        return self._invalid_dates

    @invalid_dates.setter
    def invalid_dates(self, value):
        if isinstance(value, list):
            self._invalid_dates = list()
            for i in value:
                self._invalid_dates.append(i)
    @property
    def invalid_day_in_week(self):
        return self._invalid_day_in_week

    @invalid_day_in_week.setter
    def invalid_day_in_week(self, value):
        self._invalid_day_in_week = value
    @property
    def picture(self):
        return self._picture

    @picture.setter
    def picture(self, value):
        self._picture = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def ticket_count(self):
        return self._ticket_count

    @ticket_count.setter
    def ticket_count(self, value):
        self._ticket_count = value
    @property
    def ticket_goods_id(self):
        return self._ticket_goods_id

    @ticket_goods_id.setter
    def ticket_goods_id(self, value):
        self._ticket_goods_id = value
    @property
    def ticket_link(self):
        return self._ticket_link

    @ticket_link.setter
    def ticket_link(self, value):
        self._ticket_link = value
    @property
    def ticket_name(self):
        return self._ticket_name

    @ticket_name.setter
    def ticket_name(self, value):
        self._ticket_name = value
    @property
    def ticket_no(self):
        return self._ticket_no

    @ticket_no.setter
    def ticket_no(self, value):
        self._ticket_no = value
    @property
    def ticket_specs(self):
        return self._ticket_specs

    @ticket_specs.setter
    def ticket_specs(self, value):
        self._ticket_specs = value
    @property
    def ticket_type(self):
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, value):
        self._ticket_type = value
    @property
    def ticket_use_code(self):
        return self._ticket_use_code

    @ticket_use_code.setter
    def ticket_use_code(self, value):
        self._ticket_use_code = value
    @property
    def ticket_use_pic(self):
        return self._ticket_use_pic

    @ticket_use_pic.setter
    def ticket_use_pic(self, value):
        self._ticket_use_pic = value
    @property
    def use_end_date(self):
        return self._use_end_date

    @use_end_date.setter
    def use_end_date(self, value):
        self._use_end_date = value
    @property
    def use_end_time(self):
        return self._use_end_time

    @use_end_time.setter
    def use_end_time(self, value):
        self._use_end_time = value
    @property
    def use_start_date(self):
        return self._use_start_date

    @use_start_date.setter
    def use_start_date(self, value):
        self._use_start_date = value
    @property
    def use_start_time(self):
        return self._use_start_time

    @use_start_time.setter
    def use_start_time(self, value):
        self._use_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.auto_check_time:
            if hasattr(self.auto_check_time, 'to_alipay_dict'):
                params['auto_check_time'] = self.auto_check_time.to_alipay_dict()
            else:
                params['auto_check_time'] = self.auto_check_time
        if self.check_time:
            if hasattr(self.check_time, 'to_alipay_dict'):
                params['check_time'] = self.check_time.to_alipay_dict()
            else:
                params['check_time'] = self.check_time
        if self.close_time:
            if hasattr(self.close_time, 'to_alipay_dict'):
                params['close_time'] = self.close_time.to_alipay_dict()
            else:
                params['close_time'] = self.close_time
        if self.enter_way:
            if hasattr(self.enter_way, 'to_alipay_dict'):
                params['enter_way'] = self.enter_way.to_alipay_dict()
            else:
                params['enter_way'] = self.enter_way
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.invalid_dates:
            if isinstance(self.invalid_dates, list):
                for i in range(0, len(self.invalid_dates)):
                    element = self.invalid_dates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invalid_dates[i] = element.to_alipay_dict()
            if hasattr(self.invalid_dates, 'to_alipay_dict'):
                params['invalid_dates'] = self.invalid_dates.to_alipay_dict()
            else:
                params['invalid_dates'] = self.invalid_dates
        if self.invalid_day_in_week:
            if hasattr(self.invalid_day_in_week, 'to_alipay_dict'):
                params['invalid_day_in_week'] = self.invalid_day_in_week.to_alipay_dict()
            else:
                params['invalid_day_in_week'] = self.invalid_day_in_week
        if self.picture:
            if hasattr(self.picture, 'to_alipay_dict'):
                params['picture'] = self.picture.to_alipay_dict()
            else:
                params['picture'] = self.picture
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.ticket_count:
            if hasattr(self.ticket_count, 'to_alipay_dict'):
                params['ticket_count'] = self.ticket_count.to_alipay_dict()
            else:
                params['ticket_count'] = self.ticket_count
        if self.ticket_goods_id:
            if hasattr(self.ticket_goods_id, 'to_alipay_dict'):
                params['ticket_goods_id'] = self.ticket_goods_id.to_alipay_dict()
            else:
                params['ticket_goods_id'] = self.ticket_goods_id
        if self.ticket_link:
            if hasattr(self.ticket_link, 'to_alipay_dict'):
                params['ticket_link'] = self.ticket_link.to_alipay_dict()
            else:
                params['ticket_link'] = self.ticket_link
        if self.ticket_name:
            if hasattr(self.ticket_name, 'to_alipay_dict'):
                params['ticket_name'] = self.ticket_name.to_alipay_dict()
            else:
                params['ticket_name'] = self.ticket_name
        if self.ticket_no:
            if hasattr(self.ticket_no, 'to_alipay_dict'):
                params['ticket_no'] = self.ticket_no.to_alipay_dict()
            else:
                params['ticket_no'] = self.ticket_no
        if self.ticket_specs:
            if hasattr(self.ticket_specs, 'to_alipay_dict'):
                params['ticket_specs'] = self.ticket_specs.to_alipay_dict()
            else:
                params['ticket_specs'] = self.ticket_specs
        if self.ticket_type:
            if hasattr(self.ticket_type, 'to_alipay_dict'):
                params['ticket_type'] = self.ticket_type.to_alipay_dict()
            else:
                params['ticket_type'] = self.ticket_type
        if self.ticket_use_code:
            if hasattr(self.ticket_use_code, 'to_alipay_dict'):
                params['ticket_use_code'] = self.ticket_use_code.to_alipay_dict()
            else:
                params['ticket_use_code'] = self.ticket_use_code
        if self.ticket_use_pic:
            if hasattr(self.ticket_use_pic, 'to_alipay_dict'):
                params['ticket_use_pic'] = self.ticket_use_pic.to_alipay_dict()
            else:
                params['ticket_use_pic'] = self.ticket_use_pic
        if self.use_end_date:
            if hasattr(self.use_end_date, 'to_alipay_dict'):
                params['use_end_date'] = self.use_end_date.to_alipay_dict()
            else:
                params['use_end_date'] = self.use_end_date
        if self.use_end_time:
            if hasattr(self.use_end_time, 'to_alipay_dict'):
                params['use_end_time'] = self.use_end_time.to_alipay_dict()
            else:
                params['use_end_time'] = self.use_end_time
        if self.use_start_date:
            if hasattr(self.use_start_date, 'to_alipay_dict'):
                params['use_start_date'] = self.use_start_date.to_alipay_dict()
            else:
                params['use_start_date'] = self.use_start_date
        if self.use_start_time:
            if hasattr(self.use_start_time, 'to_alipay_dict'):
                params['use_start_time'] = self.use_start_time.to_alipay_dict()
            else:
                params['use_start_time'] = self.use_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScenicTicketInfo()
        if 'auto_check_time' in d:
            o.auto_check_time = d['auto_check_time']
        if 'check_time' in d:
            o.check_time = d['check_time']
        if 'close_time' in d:
            o.close_time = d['close_time']
        if 'enter_way' in d:
            o.enter_way = d['enter_way']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'invalid_dates' in d:
            o.invalid_dates = d['invalid_dates']
        if 'invalid_day_in_week' in d:
            o.invalid_day_in_week = d['invalid_day_in_week']
        if 'picture' in d:
            o.picture = d['picture']
        if 'price' in d:
            o.price = d['price']
        if 'status' in d:
            o.status = d['status']
        if 'ticket_count' in d:
            o.ticket_count = d['ticket_count']
        if 'ticket_goods_id' in d:
            o.ticket_goods_id = d['ticket_goods_id']
        if 'ticket_link' in d:
            o.ticket_link = d['ticket_link']
        if 'ticket_name' in d:
            o.ticket_name = d['ticket_name']
        if 'ticket_no' in d:
            o.ticket_no = d['ticket_no']
        if 'ticket_specs' in d:
            o.ticket_specs = d['ticket_specs']
        if 'ticket_type' in d:
            o.ticket_type = d['ticket_type']
        if 'ticket_use_code' in d:
            o.ticket_use_code = d['ticket_use_code']
        if 'ticket_use_pic' in d:
            o.ticket_use_pic = d['ticket_use_pic']
        if 'use_end_date' in d:
            o.use_end_date = d['use_end_date']
        if 'use_end_time' in d:
            o.use_end_time = d['use_end_time']
        if 'use_start_date' in d:
            o.use_start_date = d['use_start_date']
        if 'use_start_time' in d:
            o.use_start_time = d['use_start_time']
        return o


