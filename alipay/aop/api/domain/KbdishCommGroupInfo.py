#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishCommGroupDetailInfo import KbdishCommGroupDetailInfo


class KbdishCommGroupInfo(object):

    def __init__(self):
        self._comm_group_id = None
        self._create_user = None
        self._ext_info = None
        self._group_desc = None
        self._group_name = None
        self._group_type = None
        self._kbdish_comm_group_detail_info_list = None
        self._merchant_id = None
        self._update_user = None
        self._view_tag = None

    @property
    def comm_group_id(self):
        return self._comm_group_id

    @comm_group_id.setter
    def comm_group_id(self, value):
        self._comm_group_id = value
    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def group_desc(self):
        return self._group_desc

    @group_desc.setter
    def group_desc(self, value):
        self._group_desc = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def group_type(self):
        return self._group_type

    @group_type.setter
    def group_type(self, value):
        self._group_type = value
    @property
    def kbdish_comm_group_detail_info_list(self):
        return self._kbdish_comm_group_detail_info_list

    @kbdish_comm_group_detail_info_list.setter
    def kbdish_comm_group_detail_info_list(self, value):
        if isinstance(value, list):
            self._kbdish_comm_group_detail_info_list = list()
            for i in value:
                if isinstance(i, KbdishCommGroupDetailInfo):
                    self._kbdish_comm_group_detail_info_list.append(i)
                else:
                    self._kbdish_comm_group_detail_info_list.append(KbdishCommGroupDetailInfo.from_alipay_dict(i))
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value
    @property
    def view_tag(self):
        return self._view_tag

    @view_tag.setter
    def view_tag(self, value):
        self._view_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.comm_group_id:
            if hasattr(self.comm_group_id, 'to_alipay_dict'):
                params['comm_group_id'] = self.comm_group_id.to_alipay_dict()
            else:
                params['comm_group_id'] = self.comm_group_id
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.group_desc:
            if hasattr(self.group_desc, 'to_alipay_dict'):
                params['group_desc'] = self.group_desc.to_alipay_dict()
            else:
                params['group_desc'] = self.group_desc
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.group_type:
            if hasattr(self.group_type, 'to_alipay_dict'):
                params['group_type'] = self.group_type.to_alipay_dict()
            else:
                params['group_type'] = self.group_type
        if self.kbdish_comm_group_detail_info_list:
            if isinstance(self.kbdish_comm_group_detail_info_list, list):
                for i in range(0, len(self.kbdish_comm_group_detail_info_list)):
                    element = self.kbdish_comm_group_detail_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.kbdish_comm_group_detail_info_list[i] = element.to_alipay_dict()
            if hasattr(self.kbdish_comm_group_detail_info_list, 'to_alipay_dict'):
                params['kbdish_comm_group_detail_info_list'] = self.kbdish_comm_group_detail_info_list.to_alipay_dict()
            else:
                params['kbdish_comm_group_detail_info_list'] = self.kbdish_comm_group_detail_info_list
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        if self.view_tag:
            if hasattr(self.view_tag, 'to_alipay_dict'):
                params['view_tag'] = self.view_tag.to_alipay_dict()
            else:
                params['view_tag'] = self.view_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishCommGroupInfo()
        if 'comm_group_id' in d:
            o.comm_group_id = d['comm_group_id']
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'group_desc' in d:
            o.group_desc = d['group_desc']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'group_type' in d:
            o.group_type = d['group_type']
        if 'kbdish_comm_group_detail_info_list' in d:
            o.kbdish_comm_group_detail_info_list = d['kbdish_comm_group_detail_info_list']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'update_user' in d:
            o.update_user = d['update_user']
        if 'view_tag' in d:
            o.view_tag = d['view_tag']
        return o


