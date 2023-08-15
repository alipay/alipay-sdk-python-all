#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialAntiepRightsSendModel(object):

    def __init__(self):
        self._biz_date = None
        self._biz_no = None
        self._rights_id = None
        self._rights_num = None
        self._source = None
        self._source_detail_type = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def rights_id(self):
        return self._rights_id

    @rights_id.setter
    def rights_id(self, value):
        self._rights_id = value
    @property
    def rights_num(self):
        return self._rights_num

    @rights_num.setter
    def rights_num(self, value):
        self._rights_num = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def source_detail_type(self):
        return self._source_detail_type

    @source_detail_type.setter
    def source_detail_type(self, value):
        self._source_detail_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.rights_id:
            if hasattr(self.rights_id, 'to_alipay_dict'):
                params['rights_id'] = self.rights_id.to_alipay_dict()
            else:
                params['rights_id'] = self.rights_id
        if self.rights_num:
            if hasattr(self.rights_num, 'to_alipay_dict'):
                params['rights_num'] = self.rights_num.to_alipay_dict()
            else:
                params['rights_num'] = self.rights_num
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.source_detail_type:
            if hasattr(self.source_detail_type, 'to_alipay_dict'):
                params['source_detail_type'] = self.source_detail_type.to_alipay_dict()
            else:
                params['source_detail_type'] = self.source_detail_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialAntiepRightsSendModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'rights_id' in d:
            o.rights_id = d['rights_id']
        if 'rights_num' in d:
            o.rights_num = d['rights_num']
        if 'source' in d:
            o.source = d['source']
        if 'source_detail_type' in d:
            o.source_detail_type = d['source_detail_type']
        return o


