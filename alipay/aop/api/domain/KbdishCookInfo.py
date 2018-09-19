#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishCookDetailInfo import KbdishCookDetailInfo


class KbdishCookInfo(object):

    def __init__(self):
        self._area = None
        self._cook_channel = None
        self._cook_ext_content = None
        self._cook_id = None
        self._cook_name = None
        self._cook_version = None
        self._create_user = None
        self._end_date = None
        self._end_time = None
        self._gmt_create = None
        self._gmt_modified = None
        self._kb_cook_detail_list = None
        self._merchant_id = None
        self._period_type = None
        self._period_value = None
        self._remarks = None
        self._shop_list = None
        self._source_from = None
        self._start_date = None
        self._start_time = None
        self._status = None
        self._update_user = None

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def cook_channel(self):
        return self._cook_channel

    @cook_channel.setter
    def cook_channel(self, value):
        self._cook_channel = value
    @property
    def cook_ext_content(self):
        return self._cook_ext_content

    @cook_ext_content.setter
    def cook_ext_content(self, value):
        self._cook_ext_content = value
    @property
    def cook_id(self):
        return self._cook_id

    @cook_id.setter
    def cook_id(self, value):
        self._cook_id = value
    @property
    def cook_name(self):
        return self._cook_name

    @cook_name.setter
    def cook_name(self, value):
        self._cook_name = value
    @property
    def cook_version(self):
        return self._cook_version

    @cook_version.setter
    def cook_version(self, value):
        self._cook_version = value
    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def kb_cook_detail_list(self):
        return self._kb_cook_detail_list

    @kb_cook_detail_list.setter
    def kb_cook_detail_list(self, value):
        if isinstance(value, list):
            self._kb_cook_detail_list = list()
            for i in value:
                if isinstance(i, KbdishCookDetailInfo):
                    self._kb_cook_detail_list.append(i)
                else:
                    self._kb_cook_detail_list.append(KbdishCookDetailInfo.from_alipay_dict(i))
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value
    @property
    def period_value(self):
        return self._period_value

    @period_value.setter
    def period_value(self, value):
        self._period_value = value
    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value
    @property
    def shop_list(self):
        return self._shop_list

    @shop_list.setter
    def shop_list(self, value):
        if isinstance(value, list):
            self._shop_list = list()
            for i in value:
                self._shop_list.append(i)
    @property
    def source_from(self):
        return self._source_from

    @source_from.setter
    def source_from(self, value):
        self._source_from = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.cook_channel:
            if hasattr(self.cook_channel, 'to_alipay_dict'):
                params['cook_channel'] = self.cook_channel.to_alipay_dict()
            else:
                params['cook_channel'] = self.cook_channel
        if self.cook_ext_content:
            if hasattr(self.cook_ext_content, 'to_alipay_dict'):
                params['cook_ext_content'] = self.cook_ext_content.to_alipay_dict()
            else:
                params['cook_ext_content'] = self.cook_ext_content
        if self.cook_id:
            if hasattr(self.cook_id, 'to_alipay_dict'):
                params['cook_id'] = self.cook_id.to_alipay_dict()
            else:
                params['cook_id'] = self.cook_id
        if self.cook_name:
            if hasattr(self.cook_name, 'to_alipay_dict'):
                params['cook_name'] = self.cook_name.to_alipay_dict()
            else:
                params['cook_name'] = self.cook_name
        if self.cook_version:
            if hasattr(self.cook_version, 'to_alipay_dict'):
                params['cook_version'] = self.cook_version.to_alipay_dict()
            else:
                params['cook_version'] = self.cook_version
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.kb_cook_detail_list:
            if isinstance(self.kb_cook_detail_list, list):
                for i in range(0, len(self.kb_cook_detail_list)):
                    element = self.kb_cook_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.kb_cook_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.kb_cook_detail_list, 'to_alipay_dict'):
                params['kb_cook_detail_list'] = self.kb_cook_detail_list.to_alipay_dict()
            else:
                params['kb_cook_detail_list'] = self.kb_cook_detail_list
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        if self.period_value:
            if hasattr(self.period_value, 'to_alipay_dict'):
                params['period_value'] = self.period_value.to_alipay_dict()
            else:
                params['period_value'] = self.period_value
        if self.remarks:
            if hasattr(self.remarks, 'to_alipay_dict'):
                params['remarks'] = self.remarks.to_alipay_dict()
            else:
                params['remarks'] = self.remarks
        if self.shop_list:
            if isinstance(self.shop_list, list):
                for i in range(0, len(self.shop_list)):
                    element = self.shop_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_list, 'to_alipay_dict'):
                params['shop_list'] = self.shop_list.to_alipay_dict()
            else:
                params['shop_list'] = self.shop_list
        if self.source_from:
            if hasattr(self.source_from, 'to_alipay_dict'):
                params['source_from'] = self.source_from.to_alipay_dict()
            else:
                params['source_from'] = self.source_from
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishCookInfo()
        if 'area' in d:
            o.area = d['area']
        if 'cook_channel' in d:
            o.cook_channel = d['cook_channel']
        if 'cook_ext_content' in d:
            o.cook_ext_content = d['cook_ext_content']
        if 'cook_id' in d:
            o.cook_id = d['cook_id']
        if 'cook_name' in d:
            o.cook_name = d['cook_name']
        if 'cook_version' in d:
            o.cook_version = d['cook_version']
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'kb_cook_detail_list' in d:
            o.kb_cook_detail_list = d['kb_cook_detail_list']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'period_type' in d:
            o.period_type = d['period_type']
        if 'period_value' in d:
            o.period_value = d['period_value']
        if 'remarks' in d:
            o.remarks = d['remarks']
        if 'shop_list' in d:
            o.shop_list = d['shop_list']
        if 'source_from' in d:
            o.source_from = d['source_from']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


