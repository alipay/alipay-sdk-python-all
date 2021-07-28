#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderExtInfo import OrderExtInfo
from alipay.aop.api.domain.OrderJourneyElement import OrderJourneyElement


class OrderJourneyInfo(object):

    def __init__(self):
        self._action = None
        self._ext_info = None
        self._journey_create_time = None
        self._journey_desc = None
        self._journey_elements = None
        self._journey_index = None
        self._journey_modify_time = None
        self._merchant_journey_no = None
        self._status = None
        self._status_desc = None
        self._sub_type = None
        self._title = None
        self._type = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, OrderExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(OrderExtInfo.from_alipay_dict(i))
    @property
    def journey_create_time(self):
        return self._journey_create_time

    @journey_create_time.setter
    def journey_create_time(self, value):
        self._journey_create_time = value
    @property
    def journey_desc(self):
        return self._journey_desc

    @journey_desc.setter
    def journey_desc(self, value):
        self._journey_desc = value
    @property
    def journey_elements(self):
        return self._journey_elements

    @journey_elements.setter
    def journey_elements(self, value):
        if isinstance(value, list):
            self._journey_elements = list()
            for i in value:
                if isinstance(i, OrderJourneyElement):
                    self._journey_elements.append(i)
                else:
                    self._journey_elements.append(OrderJourneyElement.from_alipay_dict(i))
    @property
    def journey_index(self):
        return self._journey_index

    @journey_index.setter
    def journey_index(self, value):
        self._journey_index = value
    @property
    def journey_modify_time(self):
        return self._journey_modify_time

    @journey_modify_time.setter
    def journey_modify_time(self, value):
        self._journey_modify_time = value
    @property
    def merchant_journey_no(self):
        return self._merchant_journey_no

    @merchant_journey_no.setter
    def merchant_journey_no(self, value):
        self._merchant_journey_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
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
        if self.journey_create_time:
            if hasattr(self.journey_create_time, 'to_alipay_dict'):
                params['journey_create_time'] = self.journey_create_time.to_alipay_dict()
            else:
                params['journey_create_time'] = self.journey_create_time
        if self.journey_desc:
            if hasattr(self.journey_desc, 'to_alipay_dict'):
                params['journey_desc'] = self.journey_desc.to_alipay_dict()
            else:
                params['journey_desc'] = self.journey_desc
        if self.journey_elements:
            if isinstance(self.journey_elements, list):
                for i in range(0, len(self.journey_elements)):
                    element = self.journey_elements[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.journey_elements[i] = element.to_alipay_dict()
            if hasattr(self.journey_elements, 'to_alipay_dict'):
                params['journey_elements'] = self.journey_elements.to_alipay_dict()
            else:
                params['journey_elements'] = self.journey_elements
        if self.journey_index:
            if hasattr(self.journey_index, 'to_alipay_dict'):
                params['journey_index'] = self.journey_index.to_alipay_dict()
            else:
                params['journey_index'] = self.journey_index
        if self.journey_modify_time:
            if hasattr(self.journey_modify_time, 'to_alipay_dict'):
                params['journey_modify_time'] = self.journey_modify_time.to_alipay_dict()
            else:
                params['journey_modify_time'] = self.journey_modify_time
        if self.merchant_journey_no:
            if hasattr(self.merchant_journey_no, 'to_alipay_dict'):
                params['merchant_journey_no'] = self.merchant_journey_no.to_alipay_dict()
            else:
                params['merchant_journey_no'] = self.merchant_journey_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderJourneyInfo()
        if 'action' in d:
            o.action = d['action']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'journey_create_time' in d:
            o.journey_create_time = d['journey_create_time']
        if 'journey_desc' in d:
            o.journey_desc = d['journey_desc']
        if 'journey_elements' in d:
            o.journey_elements = d['journey_elements']
        if 'journey_index' in d:
            o.journey_index = d['journey_index']
        if 'journey_modify_time' in d:
            o.journey_modify_time = d['journey_modify_time']
        if 'merchant_journey_no' in d:
            o.merchant_journey_no = d['merchant_journey_no']
        if 'status' in d:
            o.status = d['status']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        return o


