#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingSharetokenCreateModel(object):

    def __init__(self):
        self._biz_linked_id = None
        self._biz_type = None
        self._btn_left = None
        self._btn_left_href = None
        self._btn_right = None
        self._btn_right_href = None
        self._desc = None
        self._icon = None
        self._start_date = None
        self._timeout = None
        self._title = None

    @property
    def biz_linked_id(self):
        return self._biz_linked_id

    @biz_linked_id.setter
    def biz_linked_id(self, value):
        self._biz_linked_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def btn_left(self):
        return self._btn_left

    @btn_left.setter
    def btn_left(self, value):
        self._btn_left = value
    @property
    def btn_left_href(self):
        return self._btn_left_href

    @btn_left_href.setter
    def btn_left_href(self, value):
        self._btn_left_href = value
    @property
    def btn_right(self):
        return self._btn_right

    @btn_right.setter
    def btn_right(self, value):
        self._btn_right = value
    @property
    def btn_right_href(self):
        return self._btn_right_href

    @btn_right_href.setter
    def btn_right_href(self, value):
        self._btn_right_href = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_linked_id:
            if hasattr(self.biz_linked_id, 'to_alipay_dict'):
                params['biz_linked_id'] = self.biz_linked_id.to_alipay_dict()
            else:
                params['biz_linked_id'] = self.biz_linked_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.btn_left:
            if hasattr(self.btn_left, 'to_alipay_dict'):
                params['btn_left'] = self.btn_left.to_alipay_dict()
            else:
                params['btn_left'] = self.btn_left
        if self.btn_left_href:
            if hasattr(self.btn_left_href, 'to_alipay_dict'):
                params['btn_left_href'] = self.btn_left_href.to_alipay_dict()
            else:
                params['btn_left_href'] = self.btn_left_href
        if self.btn_right:
            if hasattr(self.btn_right, 'to_alipay_dict'):
                params['btn_right'] = self.btn_right.to_alipay_dict()
            else:
                params['btn_right'] = self.btn_right
        if self.btn_right_href:
            if hasattr(self.btn_right_href, 'to_alipay_dict'):
                params['btn_right_href'] = self.btn_right_href.to_alipay_dict()
            else:
                params['btn_right_href'] = self.btn_right_href
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.timeout:
            if hasattr(self.timeout, 'to_alipay_dict'):
                params['timeout'] = self.timeout.to_alipay_dict()
            else:
                params['timeout'] = self.timeout
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingSharetokenCreateModel()
        if 'biz_linked_id' in d:
            o.biz_linked_id = d['biz_linked_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'btn_left' in d:
            o.btn_left = d['btn_left']
        if 'btn_left_href' in d:
            o.btn_left_href = d['btn_left_href']
        if 'btn_right' in d:
            o.btn_right = d['btn_right']
        if 'btn_right_href' in d:
            o.btn_right_href = d['btn_right_href']
        if 'desc' in d:
            o.desc = d['desc']
        if 'icon' in d:
            o.icon = d['icon']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'timeout' in d:
            o.timeout = d['timeout']
        if 'title' in d:
            o.title = d['title']
        return o


