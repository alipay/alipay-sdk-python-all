#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AttachmentFileInfo import AttachmentFileInfo
from alipay.aop.api.domain.MetaData import MetaData


class ContractChangeSyncRequest(object):

    def __init__(self):
        self._attachment_file_info = None
        self._biz_scene = None
        self._change_type = None
        self._contract_id = None
        self._contract_name = None
        self._contract_source = None
        self._domain = None
        self._meta_datas = None
        self._sync_mode = None
        self._sys_source = None

    @property
    def attachment_file_info(self):
        return self._attachment_file_info

    @attachment_file_info.setter
    def attachment_file_info(self, value):
        if isinstance(value, AttachmentFileInfo):
            self._attachment_file_info = value
        else:
            self._attachment_file_info = AttachmentFileInfo.from_alipay_dict(value)
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def change_type(self):
        return self._change_type

    @change_type.setter
    def change_type(self, value):
        self._change_type = value
    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def contract_source(self):
        return self._contract_source

    @contract_source.setter
    def contract_source(self, value):
        self._contract_source = value
    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value
    @property
    def meta_datas(self):
        return self._meta_datas

    @meta_datas.setter
    def meta_datas(self, value):
        if isinstance(value, list):
            self._meta_datas = list()
            for i in value:
                if isinstance(i, MetaData):
                    self._meta_datas.append(i)
                else:
                    self._meta_datas.append(MetaData.from_alipay_dict(i))
    @property
    def sync_mode(self):
        return self._sync_mode

    @sync_mode.setter
    def sync_mode(self, value):
        self._sync_mode = value
    @property
    def sys_source(self):
        return self._sys_source

    @sys_source.setter
    def sys_source(self, value):
        self._sys_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_file_info:
            if hasattr(self.attachment_file_info, 'to_alipay_dict'):
                params['attachment_file_info'] = self.attachment_file_info.to_alipay_dict()
            else:
                params['attachment_file_info'] = self.attachment_file_info
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.change_type:
            if hasattr(self.change_type, 'to_alipay_dict'):
                params['change_type'] = self.change_type.to_alipay_dict()
            else:
                params['change_type'] = self.change_type
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.contract_source:
            if hasattr(self.contract_source, 'to_alipay_dict'):
                params['contract_source'] = self.contract_source.to_alipay_dict()
            else:
                params['contract_source'] = self.contract_source
        if self.domain:
            if hasattr(self.domain, 'to_alipay_dict'):
                params['domain'] = self.domain.to_alipay_dict()
            else:
                params['domain'] = self.domain
        if self.meta_datas:
            if isinstance(self.meta_datas, list):
                for i in range(0, len(self.meta_datas)):
                    element = self.meta_datas[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.meta_datas[i] = element.to_alipay_dict()
            if hasattr(self.meta_datas, 'to_alipay_dict'):
                params['meta_datas'] = self.meta_datas.to_alipay_dict()
            else:
                params['meta_datas'] = self.meta_datas
        if self.sync_mode:
            if hasattr(self.sync_mode, 'to_alipay_dict'):
                params['sync_mode'] = self.sync_mode.to_alipay_dict()
            else:
                params['sync_mode'] = self.sync_mode
        if self.sys_source:
            if hasattr(self.sys_source, 'to_alipay_dict'):
                params['sys_source'] = self.sys_source.to_alipay_dict()
            else:
                params['sys_source'] = self.sys_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractChangeSyncRequest()
        if 'attachment_file_info' in d:
            o.attachment_file_info = d['attachment_file_info']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'change_type' in d:
            o.change_type = d['change_type']
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'contract_source' in d:
            o.contract_source = d['contract_source']
        if 'domain' in d:
            o.domain = d['domain']
        if 'meta_datas' in d:
            o.meta_datas = d['meta_datas']
        if 'sync_mode' in d:
            o.sync_mode = d['sync_mode']
        if 'sys_source' in d:
            o.sys_source = d['sys_source']
        return o


