#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetManagementDetail import AssetManagementDetail


class AssetSupplyDetail(object):

    def __init__(self):
        self._apply_type = None
        self._assemble_type = None
        self._management_details = None

    @property
    def apply_type(self):
        return self._apply_type

    @apply_type.setter
    def apply_type(self, value):
        self._apply_type = value
    @property
    def assemble_type(self):
        return self._assemble_type

    @assemble_type.setter
    def assemble_type(self, value):
        self._assemble_type = value
    @property
    def management_details(self):
        return self._management_details

    @management_details.setter
    def management_details(self, value):
        if isinstance(value, list):
            self._management_details = list()
            for i in value:
                if isinstance(i, AssetManagementDetail):
                    self._management_details.append(i)
                else:
                    self._management_details.append(AssetManagementDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.apply_type:
            if hasattr(self.apply_type, 'to_alipay_dict'):
                params['apply_type'] = self.apply_type.to_alipay_dict()
            else:
                params['apply_type'] = self.apply_type
        if self.assemble_type:
            if hasattr(self.assemble_type, 'to_alipay_dict'):
                params['assemble_type'] = self.assemble_type.to_alipay_dict()
            else:
                params['assemble_type'] = self.assemble_type
        if self.management_details:
            if isinstance(self.management_details, list):
                for i in range(0, len(self.management_details)):
                    element = self.management_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.management_details[i] = element.to_alipay_dict()
            if hasattr(self.management_details, 'to_alipay_dict'):
                params['management_details'] = self.management_details.to_alipay_dict()
            else:
                params['management_details'] = self.management_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetSupplyDetail()
        if 'apply_type' in d:
            o.apply_type = d['apply_type']
        if 'assemble_type' in d:
            o.assemble_type = d['assemble_type']
        if 'management_details' in d:
            o.management_details = d['management_details']
        return o


