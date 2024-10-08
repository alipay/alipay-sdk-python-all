#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceYuntaskSupervisortaskSubmitModel(object):

    def __init__(self):
        self._phone_num = None
        self._pic_url = None
        self._shop_id = None
        self._supervisor_id = None
        self._task_instance_id = None

    @property
    def phone_num(self):
        return self._phone_num

    @phone_num.setter
    def phone_num(self, value):
        self._phone_num = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        if isinstance(value, list):
            self._pic_url = list()
            for i in value:
                self._pic_url.append(i)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def supervisor_id(self):
        return self._supervisor_id

    @supervisor_id.setter
    def supervisor_id(self, value):
        self._supervisor_id = value
    @property
    def task_instance_id(self):
        return self._task_instance_id

    @task_instance_id.setter
    def task_instance_id(self, value):
        self._task_instance_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.phone_num:
            if hasattr(self.phone_num, 'to_alipay_dict'):
                params['phone_num'] = self.phone_num.to_alipay_dict()
            else:
                params['phone_num'] = self.phone_num
        if self.pic_url:
            if isinstance(self.pic_url, list):
                for i in range(0, len(self.pic_url)):
                    element = self.pic_url[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pic_url[i] = element.to_alipay_dict()
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.supervisor_id:
            if hasattr(self.supervisor_id, 'to_alipay_dict'):
                params['supervisor_id'] = self.supervisor_id.to_alipay_dict()
            else:
                params['supervisor_id'] = self.supervisor_id
        if self.task_instance_id:
            if hasattr(self.task_instance_id, 'to_alipay_dict'):
                params['task_instance_id'] = self.task_instance_id.to_alipay_dict()
            else:
                params['task_instance_id'] = self.task_instance_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceYuntaskSupervisortaskSubmitModel()
        if 'phone_num' in d:
            o.phone_num = d['phone_num']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'supervisor_id' in d:
            o.supervisor_id = d['supervisor_id']
        if 'task_instance_id' in d:
            o.task_instance_id = d['task_instance_id']
        return o


