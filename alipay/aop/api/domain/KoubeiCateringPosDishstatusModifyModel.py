#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosDishstatusModifyModel(object):

    def __init__(self):
        self._dish_ids = None
        self._status = None

    @property
    def dish_ids(self):
        return self._dish_ids

    @dish_ids.setter
    def dish_ids(self, value):
        if isinstance(value, list):
            self._dish_ids = list()
            for i in value:
                self._dish_ids.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.dish_ids:
            if isinstance(self.dish_ids, list):
                for i in range(0, len(self.dish_ids)):
                    element = self.dish_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_ids[i] = element.to_alipay_dict()
            if hasattr(self.dish_ids, 'to_alipay_dict'):
                params['dish_ids'] = self.dish_ids.to_alipay_dict()
            else:
                params['dish_ids'] = self.dish_ids
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosDishstatusModifyModel()
        if 'dish_ids' in d:
            o.dish_ids = d['dish_ids']
        if 'status' in d:
            o.status = d['status']
        return o


