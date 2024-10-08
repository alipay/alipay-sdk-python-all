#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContactWayInfo import ContactWayInfo


class ContactPerson(object):

    def __init__(self):
        self._contact_ways = None
        self._name = None

    @property
    def contact_ways(self):
        return self._contact_ways

    @contact_ways.setter
    def contact_ways(self, value):
        if isinstance(value, list):
            self._contact_ways = list()
            for i in value:
                if isinstance(i, ContactWayInfo):
                    self._contact_ways.append(i)
                else:
                    self._contact_ways.append(ContactWayInfo.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_ways:
            if isinstance(self.contact_ways, list):
                for i in range(0, len(self.contact_ways)):
                    element = self.contact_ways[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_ways[i] = element.to_alipay_dict()
            if hasattr(self.contact_ways, 'to_alipay_dict'):
                params['contact_ways'] = self.contact_ways.to_alipay_dict()
            else:
                params['contact_ways'] = self.contact_ways
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContactPerson()
        if 'contact_ways' in d:
            o.contact_ways = d['contact_ways']
        if 'name' in d:
            o.name = d['name']
        return o


