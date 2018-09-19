#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserPassGrouplistQueryModel(object):

    def __init__(self):
        self._city_code = None
        self._group_type = None
        self._need_shopinfo = None
        self._page_num = None
        self._page_size = None
        self._partner_id = None
        self._time_status = None
        self._user_id = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def group_type(self):
        return self._group_type

    @group_type.setter
    def group_type(self, value):
        self._group_type = value
    @property
    def need_shopinfo(self):
        return self._need_shopinfo

    @need_shopinfo.setter
    def need_shopinfo(self, value):
        self._need_shopinfo = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def time_status(self):
        return self._time_status

    @time_status.setter
    def time_status(self, value):
        self._time_status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.group_type:
            if hasattr(self.group_type, 'to_alipay_dict'):
                params['group_type'] = self.group_type.to_alipay_dict()
            else:
                params['group_type'] = self.group_type
        if self.need_shopinfo:
            if hasattr(self.need_shopinfo, 'to_alipay_dict'):
                params['need_shopinfo'] = self.need_shopinfo.to_alipay_dict()
            else:
                params['need_shopinfo'] = self.need_shopinfo
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.time_status:
            if hasattr(self.time_status, 'to_alipay_dict'):
                params['time_status'] = self.time_status.to_alipay_dict()
            else:
                params['time_status'] = self.time_status
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserPassGrouplistQueryModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'group_type' in d:
            o.group_type = d['group_type']
        if 'need_shopinfo' in d:
            o.need_shopinfo = d['need_shopinfo']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'time_status' in d:
            o.time_status = d['time_status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


