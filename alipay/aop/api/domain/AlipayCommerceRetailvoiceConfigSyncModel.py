#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoiceContent import VoiceContent


class AlipayCommerceRetailvoiceConfigSyncModel(object):

    def __init__(self):
        self._advertiser_name = None
        self._delivery_end_time = None
        self._delivery_start_time = None
        self._expected_sn_count = None
        self._material_ids = None
        self._scope_file_id = None
        self._scope_type = None
        self._source_task_id = None
        self._source_version = None
        self._template_type = None
        self._touchpoint_type = None
        self._voice_content_list = None

    @property
    def advertiser_name(self):
        return self._advertiser_name

    @advertiser_name.setter
    def advertiser_name(self, value):
        self._advertiser_name = value
    @property
    def delivery_end_time(self):
        return self._delivery_end_time

    @delivery_end_time.setter
    def delivery_end_time(self, value):
        self._delivery_end_time = value
    @property
    def delivery_start_time(self):
        return self._delivery_start_time

    @delivery_start_time.setter
    def delivery_start_time(self, value):
        self._delivery_start_time = value
    @property
    def expected_sn_count(self):
        return self._expected_sn_count

    @expected_sn_count.setter
    def expected_sn_count(self, value):
        self._expected_sn_count = value
    @property
    def material_ids(self):
        return self._material_ids

    @material_ids.setter
    def material_ids(self, value):
        if isinstance(value, list):
            self._material_ids = list()
            for i in value:
                self._material_ids.append(i)
    @property
    def scope_file_id(self):
        return self._scope_file_id

    @scope_file_id.setter
    def scope_file_id(self, value):
        self._scope_file_id = value
    @property
    def scope_type(self):
        return self._scope_type

    @scope_type.setter
    def scope_type(self, value):
        self._scope_type = value
    @property
    def source_task_id(self):
        return self._source_task_id

    @source_task_id.setter
    def source_task_id(self, value):
        self._source_task_id = value
    @property
    def source_version(self):
        return self._source_version

    @source_version.setter
    def source_version(self, value):
        self._source_version = value
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value
    @property
    def touchpoint_type(self):
        return self._touchpoint_type

    @touchpoint_type.setter
    def touchpoint_type(self, value):
        self._touchpoint_type = value
    @property
    def voice_content_list(self):
        return self._voice_content_list

    @voice_content_list.setter
    def voice_content_list(self, value):
        if isinstance(value, list):
            self._voice_content_list = list()
            for i in value:
                if isinstance(i, VoiceContent):
                    self._voice_content_list.append(i)
                else:
                    self._voice_content_list.append(VoiceContent.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.advertiser_name:
            if hasattr(self.advertiser_name, 'to_alipay_dict'):
                params['advertiser_name'] = self.advertiser_name.to_alipay_dict()
            else:
                params['advertiser_name'] = self.advertiser_name
        if self.delivery_end_time:
            if hasattr(self.delivery_end_time, 'to_alipay_dict'):
                params['delivery_end_time'] = self.delivery_end_time.to_alipay_dict()
            else:
                params['delivery_end_time'] = self.delivery_end_time
        if self.delivery_start_time:
            if hasattr(self.delivery_start_time, 'to_alipay_dict'):
                params['delivery_start_time'] = self.delivery_start_time.to_alipay_dict()
            else:
                params['delivery_start_time'] = self.delivery_start_time
        if self.expected_sn_count:
            if hasattr(self.expected_sn_count, 'to_alipay_dict'):
                params['expected_sn_count'] = self.expected_sn_count.to_alipay_dict()
            else:
                params['expected_sn_count'] = self.expected_sn_count
        if self.material_ids:
            if isinstance(self.material_ids, list):
                for i in range(0, len(self.material_ids)):
                    element = self.material_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.material_ids[i] = element.to_alipay_dict()
            if hasattr(self.material_ids, 'to_alipay_dict'):
                params['material_ids'] = self.material_ids.to_alipay_dict()
            else:
                params['material_ids'] = self.material_ids
        if self.scope_file_id:
            if hasattr(self.scope_file_id, 'to_alipay_dict'):
                params['scope_file_id'] = self.scope_file_id.to_alipay_dict()
            else:
                params['scope_file_id'] = self.scope_file_id
        if self.scope_type:
            if hasattr(self.scope_type, 'to_alipay_dict'):
                params['scope_type'] = self.scope_type.to_alipay_dict()
            else:
                params['scope_type'] = self.scope_type
        if self.source_task_id:
            if hasattr(self.source_task_id, 'to_alipay_dict'):
                params['source_task_id'] = self.source_task_id.to_alipay_dict()
            else:
                params['source_task_id'] = self.source_task_id
        if self.source_version:
            if hasattr(self.source_version, 'to_alipay_dict'):
                params['source_version'] = self.source_version.to_alipay_dict()
            else:
                params['source_version'] = self.source_version
        if self.template_type:
            if hasattr(self.template_type, 'to_alipay_dict'):
                params['template_type'] = self.template_type.to_alipay_dict()
            else:
                params['template_type'] = self.template_type
        if self.touchpoint_type:
            if hasattr(self.touchpoint_type, 'to_alipay_dict'):
                params['touchpoint_type'] = self.touchpoint_type.to_alipay_dict()
            else:
                params['touchpoint_type'] = self.touchpoint_type
        if self.voice_content_list:
            if isinstance(self.voice_content_list, list):
                for i in range(0, len(self.voice_content_list)):
                    element = self.voice_content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voice_content_list[i] = element.to_alipay_dict()
            if hasattr(self.voice_content_list, 'to_alipay_dict'):
                params['voice_content_list'] = self.voice_content_list.to_alipay_dict()
            else:
                params['voice_content_list'] = self.voice_content_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailvoiceConfigSyncModel()
        if 'advertiser_name' in d:
            o.advertiser_name = d['advertiser_name']
        if 'delivery_end_time' in d:
            o.delivery_end_time = d['delivery_end_time']
        if 'delivery_start_time' in d:
            o.delivery_start_time = d['delivery_start_time']
        if 'expected_sn_count' in d:
            o.expected_sn_count = d['expected_sn_count']
        if 'material_ids' in d:
            o.material_ids = d['material_ids']
        if 'scope_file_id' in d:
            o.scope_file_id = d['scope_file_id']
        if 'scope_type' in d:
            o.scope_type = d['scope_type']
        if 'source_task_id' in d:
            o.source_task_id = d['source_task_id']
        if 'source_version' in d:
            o.source_version = d['source_version']
        if 'template_type' in d:
            o.template_type = d['template_type']
        if 'touchpoint_type' in d:
            o.touchpoint_type = d['touchpoint_type']
        if 'voice_content_list' in d:
            o.voice_content_list = d['voice_content_list']
        return o


