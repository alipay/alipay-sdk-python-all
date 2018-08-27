#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PassInfoOpenApiModel(object):

    def __init__(self):
        self._data_info = None
        self._end_date = None
        self._ext_info = None
        self._gmt_create = None
        self._item_id = None
        self._logo_text = None
        self._mechant_name = None
        self._pass_id = None
        self._second_logo_text = None
        self._shop_id_list = None
        self._start_date = None
        self._status = None

    @property
    def data_info(self):
        return self._data_info

    @data_info.setter
    def data_info(self, value):
        self._data_info = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def logo_text(self):
        return self._logo_text

    @logo_text.setter
    def logo_text(self, value):
        self._logo_text = value
    @property
    def mechant_name(self):
        return self._mechant_name

    @mechant_name.setter
    def mechant_name(self, value):
        self._mechant_name = value
    @property
    def pass_id(self):
        return self._pass_id

    @pass_id.setter
    def pass_id(self, value):
        self._pass_id = value
    @property
    def second_logo_text(self):
        return self._second_logo_text

    @second_logo_text.setter
    def second_logo_text(self, value):
        self._second_logo_text = value
    @property
    def shop_id_list(self):
        return self._shop_id_list

    @shop_id_list.setter
    def shop_id_list(self, value):
        if isinstance(value, list):
            self._shop_id_list = list()
            for i in value:
                self._shop_id_list.append(i)
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_info:
            if hasattr(self.data_info, 'to_alipay_dict'):
                params['data_info'] = self.data_info.to_alipay_dict()
            else:
                params['data_info'] = self.data_info
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.logo_text:
            if hasattr(self.logo_text, 'to_alipay_dict'):
                params['logo_text'] = self.logo_text.to_alipay_dict()
            else:
                params['logo_text'] = self.logo_text
        if self.mechant_name:
            if hasattr(self.mechant_name, 'to_alipay_dict'):
                params['mechant_name'] = self.mechant_name.to_alipay_dict()
            else:
                params['mechant_name'] = self.mechant_name
        if self.pass_id:
            if hasattr(self.pass_id, 'to_alipay_dict'):
                params['pass_id'] = self.pass_id.to_alipay_dict()
            else:
                params['pass_id'] = self.pass_id
        if self.second_logo_text:
            if hasattr(self.second_logo_text, 'to_alipay_dict'):
                params['second_logo_text'] = self.second_logo_text.to_alipay_dict()
            else:
                params['second_logo_text'] = self.second_logo_text
        if self.shop_id_list:
            if isinstance(self.shop_id_list, list):
                for i in range(0, len(self.shop_id_list)):
                    element = self.shop_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_id_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_id_list, 'to_alipay_dict'):
                params['shop_id_list'] = self.shop_id_list.to_alipay_dict()
            else:
                params['shop_id_list'] = self.shop_id_list
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
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
        o = PassInfoOpenApiModel()
        if 'data_info' in d:
            o.data_info = d['data_info']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'logo_text' in d:
            o.logo_text = d['logo_text']
        if 'mechant_name' in d:
            o.mechant_name = d['mechant_name']
        if 'pass_id' in d:
            o.pass_id = d['pass_id']
        if 'second_logo_text' in d:
            o.second_logo_text = d['second_logo_text']
        if 'shop_id_list' in d:
            o.shop_id_list = d['shop_id_list']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        return o


