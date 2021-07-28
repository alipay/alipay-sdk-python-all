#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WorldTicketType(object):

    def __init__(self):
        self._ticket_type_code = None
        self._ticket_type_desc = None
        self._ticket_type_name = None

    @property
    def ticket_type_code(self):
        return self._ticket_type_code

    @ticket_type_code.setter
    def ticket_type_code(self, value):
        self._ticket_type_code = value
    @property
    def ticket_type_desc(self):
        return self._ticket_type_desc

    @ticket_type_desc.setter
    def ticket_type_desc(self, value):
        self._ticket_type_desc = value
    @property
    def ticket_type_name(self):
        return self._ticket_type_name

    @ticket_type_name.setter
    def ticket_type_name(self, value):
        self._ticket_type_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ticket_type_code:
            if hasattr(self.ticket_type_code, 'to_alipay_dict'):
                params['ticket_type_code'] = self.ticket_type_code.to_alipay_dict()
            else:
                params['ticket_type_code'] = self.ticket_type_code
        if self.ticket_type_desc:
            if hasattr(self.ticket_type_desc, 'to_alipay_dict'):
                params['ticket_type_desc'] = self.ticket_type_desc.to_alipay_dict()
            else:
                params['ticket_type_desc'] = self.ticket_type_desc
        if self.ticket_type_name:
            if hasattr(self.ticket_type_name, 'to_alipay_dict'):
                params['ticket_type_name'] = self.ticket_type_name.to_alipay_dict()
            else:
                params['ticket_type_name'] = self.ticket_type_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WorldTicketType()
        if 'ticket_type_code' in d:
            o.ticket_type_code = d['ticket_type_code']
        if 'ticket_type_desc' in d:
            o.ticket_type_desc = d['ticket_type_desc']
        if 'ticket_type_name' in d:
            o.ticket_type_name = d['ticket_type_name']
        return o


