#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoContentApiSchemaVO(object):

    def __init__(self):
        self._demo_pic = None
        self._schema_id = None
        self._schema_xml = None

    @property
    def demo_pic(self):
        return self._demo_pic

    @demo_pic.setter
    def demo_pic(self, value):
        self._demo_pic = value
    @property
    def schema_id(self):
        return self._schema_id

    @schema_id.setter
    def schema_id(self, value):
        self._schema_id = value
    @property
    def schema_xml(self):
        return self._schema_xml

    @schema_xml.setter
    def schema_xml(self, value):
        self._schema_xml = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo_pic:
            if hasattr(self.demo_pic, 'to_alipay_dict'):
                params['demo_pic'] = self.demo_pic.to_alipay_dict()
            else:
                params['demo_pic'] = self.demo_pic
        if self.schema_id:
            if hasattr(self.schema_id, 'to_alipay_dict'):
                params['schema_id'] = self.schema_id.to_alipay_dict()
            else:
                params['schema_id'] = self.schema_id
        if self.schema_xml:
            if hasattr(self.schema_xml, 'to_alipay_dict'):
                params['schema_xml'] = self.schema_xml.to_alipay_dict()
            else:
                params['schema_xml'] = self.schema_xml
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoContentApiSchemaVO()
        if 'demo_pic' in d:
            o.demo_pic = d['demo_pic']
        if 'schema_id' in d:
            o.schema_id = d['schema_id']
        if 'schema_xml' in d:
            o.schema_xml = d['schema_xml']
        return o


