#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AvatarMultiPageConfig import AvatarMultiPageConfig


class AlipayIserviceItaskAvatarGentaskSyncModel(object):

    def __init__(self):
        self._location = None
        self._multi_page_config = None
        self._need_water_mark = None
        self._ori_text = None
        self._ori_text_list = None
        self._project_id = None
        self._resolution = None
        self._sub_title = None
        self._template_apply_all_page = None
        self._template_id = None
        self._tenant_code = None
        self._video_name = None
        self._video_type = None

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def multi_page_config(self):
        return self._multi_page_config

    @multi_page_config.setter
    def multi_page_config(self, value):
        if isinstance(value, list):
            self._multi_page_config = list()
            for i in value:
                if isinstance(i, AvatarMultiPageConfig):
                    self._multi_page_config.append(i)
                else:
                    self._multi_page_config.append(AvatarMultiPageConfig.from_alipay_dict(i))
    @property
    def need_water_mark(self):
        return self._need_water_mark

    @need_water_mark.setter
    def need_water_mark(self, value):
        self._need_water_mark = value
    @property
    def ori_text(self):
        return self._ori_text

    @ori_text.setter
    def ori_text(self, value):
        self._ori_text = value
    @property
    def ori_text_list(self):
        return self._ori_text_list

    @ori_text_list.setter
    def ori_text_list(self, value):
        if isinstance(value, list):
            self._ori_text_list = list()
            for i in value:
                self._ori_text_list.append(i)
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def resolution(self):
        return self._resolution

    @resolution.setter
    def resolution(self, value):
        self._resolution = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def template_apply_all_page(self):
        return self._template_apply_all_page

    @template_apply_all_page.setter
    def template_apply_all_page(self, value):
        self._template_apply_all_page = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value
    @property
    def video_name(self):
        return self._video_name

    @video_name.setter
    def video_name(self, value):
        self._video_name = value
    @property
    def video_type(self):
        return self._video_type

    @video_type.setter
    def video_type(self, value):
        self._video_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.multi_page_config:
            if isinstance(self.multi_page_config, list):
                for i in range(0, len(self.multi_page_config)):
                    element = self.multi_page_config[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.multi_page_config[i] = element.to_alipay_dict()
            if hasattr(self.multi_page_config, 'to_alipay_dict'):
                params['multi_page_config'] = self.multi_page_config.to_alipay_dict()
            else:
                params['multi_page_config'] = self.multi_page_config
        if self.need_water_mark:
            if hasattr(self.need_water_mark, 'to_alipay_dict'):
                params['need_water_mark'] = self.need_water_mark.to_alipay_dict()
            else:
                params['need_water_mark'] = self.need_water_mark
        if self.ori_text:
            if hasattr(self.ori_text, 'to_alipay_dict'):
                params['ori_text'] = self.ori_text.to_alipay_dict()
            else:
                params['ori_text'] = self.ori_text
        if self.ori_text_list:
            if isinstance(self.ori_text_list, list):
                for i in range(0, len(self.ori_text_list)):
                    element = self.ori_text_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ori_text_list[i] = element.to_alipay_dict()
            if hasattr(self.ori_text_list, 'to_alipay_dict'):
                params['ori_text_list'] = self.ori_text_list.to_alipay_dict()
            else:
                params['ori_text_list'] = self.ori_text_list
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.resolution:
            if hasattr(self.resolution, 'to_alipay_dict'):
                params['resolution'] = self.resolution.to_alipay_dict()
            else:
                params['resolution'] = self.resolution
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.template_apply_all_page:
            if hasattr(self.template_apply_all_page, 'to_alipay_dict'):
                params['template_apply_all_page'] = self.template_apply_all_page.to_alipay_dict()
            else:
                params['template_apply_all_page'] = self.template_apply_all_page
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        if self.video_name:
            if hasattr(self.video_name, 'to_alipay_dict'):
                params['video_name'] = self.video_name.to_alipay_dict()
            else:
                params['video_name'] = self.video_name
        if self.video_type:
            if hasattr(self.video_type, 'to_alipay_dict'):
                params['video_type'] = self.video_type.to_alipay_dict()
            else:
                params['video_type'] = self.video_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceItaskAvatarGentaskSyncModel()
        if 'location' in d:
            o.location = d['location']
        if 'multi_page_config' in d:
            o.multi_page_config = d['multi_page_config']
        if 'need_water_mark' in d:
            o.need_water_mark = d['need_water_mark']
        if 'ori_text' in d:
            o.ori_text = d['ori_text']
        if 'ori_text_list' in d:
            o.ori_text_list = d['ori_text_list']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'resolution' in d:
            o.resolution = d['resolution']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'template_apply_all_page' in d:
            o.template_apply_all_page = d['template_apply_all_page']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        if 'video_name' in d:
            o.video_name = d['video_name']
        if 'video_type' in d:
            o.video_type = d['video_type']
        return o


