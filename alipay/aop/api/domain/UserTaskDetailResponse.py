#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserTaskDetailResponse(object):

    def __init__(self):
        self._credit_no = None
        self._last_date = None
        self._out_order_no = None
        self._pay_count = None
        self._prize_name = None
        self._send_shop_name = None
        self._sign_date = None
        self._task_id = None
        self._uid = None
        self._uid_open_id = None
        self._user_task_id = None
        self._user_task_pay_status = None
        self._user_task_status = None

    @property
    def credit_no(self):
        return self._credit_no

    @credit_no.setter
    def credit_no(self, value):
        self._credit_no = value
    @property
    def last_date(self):
        return self._last_date

    @last_date.setter
    def last_date(self, value):
        self._last_date = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_count(self):
        return self._pay_count

    @pay_count.setter
    def pay_count(self, value):
        self._pay_count = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def send_shop_name(self):
        return self._send_shop_name

    @send_shop_name.setter
    def send_shop_name(self, value):
        self._send_shop_name = value
    @property
    def sign_date(self):
        return self._sign_date

    @sign_date.setter
    def sign_date(self, value):
        self._sign_date = value
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
    def user_task_id(self):
        return self._user_task_id

    @user_task_id.setter
    def user_task_id(self, value):
        self._user_task_id = value
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
        if self.credit_no:
            if hasattr(self.credit_no, 'to_alipay_dict'):
                params['credit_no'] = self.credit_no.to_alipay_dict()
            else:
                params['credit_no'] = self.credit_no
        if self.last_date:
            if hasattr(self.last_date, 'to_alipay_dict'):
                params['last_date'] = self.last_date.to_alipay_dict()
            else:
                params['last_date'] = self.last_date
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.pay_count:
            if hasattr(self.pay_count, 'to_alipay_dict'):
                params['pay_count'] = self.pay_count.to_alipay_dict()
            else:
                params['pay_count'] = self.pay_count
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.send_shop_name:
            if hasattr(self.send_shop_name, 'to_alipay_dict'):
                params['send_shop_name'] = self.send_shop_name.to_alipay_dict()
            else:
                params['send_shop_name'] = self.send_shop_name
        if self.sign_date:
            if hasattr(self.sign_date, 'to_alipay_dict'):
                params['sign_date'] = self.sign_date.to_alipay_dict()
            else:
                params['sign_date'] = self.sign_date
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
        if self.user_task_id:
            if hasattr(self.user_task_id, 'to_alipay_dict'):
                params['user_task_id'] = self.user_task_id.to_alipay_dict()
            else:
                params['user_task_id'] = self.user_task_id
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
        o = UserTaskDetailResponse()
        if 'credit_no' in d:
            o.credit_no = d['credit_no']
        if 'last_date' in d:
            o.last_date = d['last_date']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'pay_count' in d:
            o.pay_count = d['pay_count']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'send_shop_name' in d:
            o.send_shop_name = d['send_shop_name']
        if 'sign_date' in d:
            o.sign_date = d['sign_date']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'uid' in d:
            o.uid = d['uid']
        if 'uid_open_id' in d:
            o.uid_open_id = d['uid_open_id']
        if 'user_task_id' in d:
            o.user_task_id = d['user_task_id']
        if 'user_task_pay_status' in d:
            o.user_task_pay_status = d['user_task_pay_status']
        if 'user_task_status' in d:
            o.user_task_status = d['user_task_status']
        return o


