#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpContactInfo(object):

    def __init__(self):
        self._ep_contact = None

    @property
    def ep_contact(self):
        return self._ep_contact

    @ep_contact.setter
    def ep_contact(self, value):
        if isinstance(value, list):
            self._ep_contact = list()
            for i in value:
                self._ep_contact.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.ep_contact:
            if isinstance(self.ep_contact, list):
                for i in range(0, len(self.ep_contact)):
                    element = self.ep_contact[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ep_contact[i] = element.to_alipay_dict()
            if hasattr(self.ep_contact, 'to_alipay_dict'):
                params['ep_contact'] = self.ep_contact.to_alipay_dict()
            else:
                params['ep_contact'] = self.ep_contact
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpContactInfo()
        if 'ep_contact' in d:
            o.ep_contact = d['ep_contact']
        return o


