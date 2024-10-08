#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnswerItemDetail(object):

    def __init__(self):
        self._accept_conditions = None
        self._check_list = None
        self._id = None
        self._link = None
        self._location = None
        self._name = None
        self._service_item_id = None

    @property
    def accept_conditions(self):
        return self._accept_conditions

    @accept_conditions.setter
    def accept_conditions(self, value):
        self._accept_conditions = value
    @property
    def check_list(self):
        return self._check_list

    @check_list.setter
    def check_list(self, value):
        self._check_list = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def service_item_id(self):
        return self._service_item_id

    @service_item_id.setter
    def service_item_id(self, value):
        self._service_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.accept_conditions:
            if hasattr(self.accept_conditions, 'to_alipay_dict'):
                params['accept_conditions'] = self.accept_conditions.to_alipay_dict()
            else:
                params['accept_conditions'] = self.accept_conditions
        if self.check_list:
            if hasattr(self.check_list, 'to_alipay_dict'):
                params['check_list'] = self.check_list.to_alipay_dict()
            else:
                params['check_list'] = self.check_list
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.service_item_id:
            if hasattr(self.service_item_id, 'to_alipay_dict'):
                params['service_item_id'] = self.service_item_id.to_alipay_dict()
            else:
                params['service_item_id'] = self.service_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnswerItemDetail()
        if 'accept_conditions' in d:
            o.accept_conditions = d['accept_conditions']
        if 'check_list' in d:
            o.check_list = d['check_list']
        if 'id' in d:
            o.id = d['id']
        if 'link' in d:
            o.link = d['link']
        if 'location' in d:
            o.location = d['location']
        if 'name' in d:
            o.name = d['name']
        if 'service_item_id' in d:
            o.service_item_id = d['service_item_id']
        return o


