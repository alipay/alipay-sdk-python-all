#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeskEntity(object):

    def __init__(self):
        self._area_id = None
        self._desk_name = None
        self._desk_no = None
        self._id = None
        self._max_num = None
        self._qr_code_id = None
        self._relation_id = None
        self._shop_id = None
        self._sort_num = None

    @property
    def area_id(self):
        return self._area_id

    @area_id.setter
    def area_id(self, value):
        self._area_id = value
    @property
    def desk_name(self):
        return self._desk_name

    @desk_name.setter
    def desk_name(self, value):
        self._desk_name = value
    @property
    def desk_no(self):
        return self._desk_no

    @desk_no.setter
    def desk_no(self, value):
        self._desk_no = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def max_num(self):
        return self._max_num

    @max_num.setter
    def max_num(self, value):
        self._max_num = value
    @property
    def qr_code_id(self):
        return self._qr_code_id

    @qr_code_id.setter
    def qr_code_id(self, value):
        self._qr_code_id = value
    @property
    def relation_id(self):
        return self._relation_id

    @relation_id.setter
    def relation_id(self, value):
        self._relation_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sort_num(self):
        return self._sort_num

    @sort_num.setter
    def sort_num(self, value):
        self._sort_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_id:
            if hasattr(self.area_id, 'to_alipay_dict'):
                params['area_id'] = self.area_id.to_alipay_dict()
            else:
                params['area_id'] = self.area_id
        if self.desk_name:
            if hasattr(self.desk_name, 'to_alipay_dict'):
                params['desk_name'] = self.desk_name.to_alipay_dict()
            else:
                params['desk_name'] = self.desk_name
        if self.desk_no:
            if hasattr(self.desk_no, 'to_alipay_dict'):
                params['desk_no'] = self.desk_no.to_alipay_dict()
            else:
                params['desk_no'] = self.desk_no
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.max_num:
            if hasattr(self.max_num, 'to_alipay_dict'):
                params['max_num'] = self.max_num.to_alipay_dict()
            else:
                params['max_num'] = self.max_num
        if self.qr_code_id:
            if hasattr(self.qr_code_id, 'to_alipay_dict'):
                params['qr_code_id'] = self.qr_code_id.to_alipay_dict()
            else:
                params['qr_code_id'] = self.qr_code_id
        if self.relation_id:
            if hasattr(self.relation_id, 'to_alipay_dict'):
                params['relation_id'] = self.relation_id.to_alipay_dict()
            else:
                params['relation_id'] = self.relation_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sort_num:
            if hasattr(self.sort_num, 'to_alipay_dict'):
                params['sort_num'] = self.sort_num.to_alipay_dict()
            else:
                params['sort_num'] = self.sort_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeskEntity()
        if 'area_id' in d:
            o.area_id = d['area_id']
        if 'desk_name' in d:
            o.desk_name = d['desk_name']
        if 'desk_no' in d:
            o.desk_no = d['desk_no']
        if 'id' in d:
            o.id = d['id']
        if 'max_num' in d:
            o.max_num = d['max_num']
        if 'qr_code_id' in d:
            o.qr_code_id = d['qr_code_id']
        if 'relation_id' in d:
            o.relation_id = d['relation_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sort_num' in d:
            o.sort_num = d['sort_num']
        return o


