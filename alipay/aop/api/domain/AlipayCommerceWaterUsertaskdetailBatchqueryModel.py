#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceWaterUsertaskdetailBatchqueryModel(object):

    def __init__(self):
        self._end_date = None
        self._out_order_no = None
        self._page_num = None
        self._page_size = None
        self._send_shop_name = None
        self._start_date = None
        self._task_id = None
        self._uid = None
        self._uid_open_id = None
        self._user_task_pay_status = None
        self._user_task_status = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
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
    def send_shop_name(self):
        return self._send_shop_name

    @send_shop_name.setter
    def send_shop_name(self, value):
        self._send_shop_name = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def uid_open_id(self):
        return self._uid_open_id

    @uid_open_id.setter
    def uid_open_id(self, value):
        self._uid_open_id = value
    @property
    def user_task_pay_status(self):
        return self._user_task_pay_status

    @user_task_pay_status.setter
    def user_task_pay_status(self, value):
        self._user_task_pay_status = value
    @property
    def user_task_status(self):
        return self._user_task_status

    @user_task_status.setter
    def user_task_status(self, value):
        self._user_task_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
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
        if self.send_shop_name:
            if hasattr(self.send_shop_name, 'to_alipay_dict'):
                params['send_shop_name'] = self.send_shop_name.to_alipay_dict()
            else:
                params['send_shop_name'] = self.send_shop_name
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.uid_open_id:
            if hasattr(self.uid_open_id, 'to_alipay_dict'):
                params['uid_open_id'] = self.uid_open_id.to_alipay_dict()
            else:
                params['uid_open_id'] = self.uid_open_id
        if self.user_task_pay_status:
            if hasattr(self.user_task_pay_status, 'to_alipay_dict'):
                params['user_task_pay_status'] = self.user_task_pay_status.to_alipay_dict()
            else:
                params['user_task_pay_status'] = self.user_task_pay_status
        if self.user_task_status:
            if hasattr(self.user_task_status, 'to_alipay_dict'):
                params['user_task_status'] = self.user_task_status.to_alipay_dict()
            else:
                params['user_task_status'] = self.user_task_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceWaterUsertaskdetailBatchqueryModel()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'send_shop_name' in d:
            o.send_shop_name = d['send_shop_name']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'uid' in d:
            o.uid = d['uid']
        if 'uid_open_id' in d:
            o.uid_open_id = d['uid_open_id']
        if 'user_task_pay_status' in d:
            o.user_task_pay_status = d['user_task_pay_status']
        if 'user_task_status' in d:
            o.user_task_status = d['user_task_status']
        return o


