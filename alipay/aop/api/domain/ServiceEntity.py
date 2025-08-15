#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LandingTypeDto import LandingTypeDto


class ServiceEntity(object):

    def __init__(self):
        self._service_entity_app_id = None
        self._service_entity_app_name = None
        self._service_entity_app_url = None
        self._service_entity_desc = None
        self._service_entity_landing_page = None
        self._service_entity_name = None
        self._service_entity_no = None
        self._service_entity_out_id = None
        self._service_entity_out_source = None
        self._service_entity_picture = None
        self._service_entity_picture_list = None
        self._service_entity_target_url = None
        self._service_entity_target_url_snd = None
        self._service_entity_type = None
        self._service_entity_video_list = None
        self._service_entity_white_picture = None

    @property
    def service_entity_app_id(self):
        return self._service_entity_app_id

    @service_entity_app_id.setter
    def service_entity_app_id(self, value):
        self._service_entity_app_id = value
    @property
    def service_entity_app_name(self):
        return self._service_entity_app_name

    @service_entity_app_name.setter
    def service_entity_app_name(self, value):
        self._service_entity_app_name = value
    @property
    def service_entity_app_url(self):
        return self._service_entity_app_url

    @service_entity_app_url.setter
    def service_entity_app_url(self, value):
        self._service_entity_app_url = value
    @property
    def service_entity_desc(self):
        return self._service_entity_desc

    @service_entity_desc.setter
    def service_entity_desc(self, value):
        self._service_entity_desc = value
    @property
    def service_entity_landing_page(self):
        return self._service_entity_landing_page

    @service_entity_landing_page.setter
    def service_entity_landing_page(self, value):
        if isinstance(value, list):
            self._service_entity_landing_page = list()
            for i in value:
                if isinstance(i, LandingTypeDto):
                    self._service_entity_landing_page.append(i)
                else:
                    self._service_entity_landing_page.append(LandingTypeDto.from_alipay_dict(i))
    @property
    def service_entity_name(self):
        return self._service_entity_name

    @service_entity_name.setter
    def service_entity_name(self, value):
        self._service_entity_name = value
    @property
    def service_entity_no(self):
        return self._service_entity_no

    @service_entity_no.setter
    def service_entity_no(self, value):
        self._service_entity_no = value
    @property
    def service_entity_out_id(self):
        return self._service_entity_out_id

    @service_entity_out_id.setter
    def service_entity_out_id(self, value):
        self._service_entity_out_id = value
    @property
    def service_entity_out_source(self):
        return self._service_entity_out_source

    @service_entity_out_source.setter
    def service_entity_out_source(self, value):
        self._service_entity_out_source = value
    @property
    def service_entity_picture(self):
        return self._service_entity_picture

    @service_entity_picture.setter
    def service_entity_picture(self, value):
        self._service_entity_picture = value
    @property
    def service_entity_picture_list(self):
        return self._service_entity_picture_list

    @service_entity_picture_list.setter
    def service_entity_picture_list(self, value):
        if isinstance(value, list):
            self._service_entity_picture_list = list()
            for i in value:
                self._service_entity_picture_list.append(i)
    @property
    def service_entity_target_url(self):
        return self._service_entity_target_url

    @service_entity_target_url.setter
    def service_entity_target_url(self, value):
        self._service_entity_target_url = value
    @property
    def service_entity_target_url_snd(self):
        return self._service_entity_target_url_snd

    @service_entity_target_url_snd.setter
    def service_entity_target_url_snd(self, value):
        self._service_entity_target_url_snd = value
    @property
    def service_entity_type(self):
        return self._service_entity_type

    @service_entity_type.setter
    def service_entity_type(self, value):
        self._service_entity_type = value
    @property
    def service_entity_video_list(self):
        return self._service_entity_video_list

    @service_entity_video_list.setter
    def service_entity_video_list(self, value):
        if isinstance(value, list):
            self._service_entity_video_list = list()
            for i in value:
                self._service_entity_video_list.append(i)
    @property
    def service_entity_white_picture(self):
        return self._service_entity_white_picture

    @service_entity_white_picture.setter
    def service_entity_white_picture(self, value):
        self._service_entity_white_picture = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_entity_app_id:
            if hasattr(self.service_entity_app_id, 'to_alipay_dict'):
                params['service_entity_app_id'] = self.service_entity_app_id.to_alipay_dict()
            else:
                params['service_entity_app_id'] = self.service_entity_app_id
        if self.service_entity_app_name:
            if hasattr(self.service_entity_app_name, 'to_alipay_dict'):
                params['service_entity_app_name'] = self.service_entity_app_name.to_alipay_dict()
            else:
                params['service_entity_app_name'] = self.service_entity_app_name
        if self.service_entity_app_url:
            if hasattr(self.service_entity_app_url, 'to_alipay_dict'):
                params['service_entity_app_url'] = self.service_entity_app_url.to_alipay_dict()
            else:
                params['service_entity_app_url'] = self.service_entity_app_url
        if self.service_entity_desc:
            if hasattr(self.service_entity_desc, 'to_alipay_dict'):
                params['service_entity_desc'] = self.service_entity_desc.to_alipay_dict()
            else:
                params['service_entity_desc'] = self.service_entity_desc
        if self.service_entity_landing_page:
            if isinstance(self.service_entity_landing_page, list):
                for i in range(0, len(self.service_entity_landing_page)):
                    element = self.service_entity_landing_page[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_entity_landing_page[i] = element.to_alipay_dict()
            if hasattr(self.service_entity_landing_page, 'to_alipay_dict'):
                params['service_entity_landing_page'] = self.service_entity_landing_page.to_alipay_dict()
            else:
                params['service_entity_landing_page'] = self.service_entity_landing_page
        if self.service_entity_name:
            if hasattr(self.service_entity_name, 'to_alipay_dict'):
                params['service_entity_name'] = self.service_entity_name.to_alipay_dict()
            else:
                params['service_entity_name'] = self.service_entity_name
        if self.service_entity_no:
            if hasattr(self.service_entity_no, 'to_alipay_dict'):
                params['service_entity_no'] = self.service_entity_no.to_alipay_dict()
            else:
                params['service_entity_no'] = self.service_entity_no
        if self.service_entity_out_id:
            if hasattr(self.service_entity_out_id, 'to_alipay_dict'):
                params['service_entity_out_id'] = self.service_entity_out_id.to_alipay_dict()
            else:
                params['service_entity_out_id'] = self.service_entity_out_id
        if self.service_entity_out_source:
            if hasattr(self.service_entity_out_source, 'to_alipay_dict'):
                params['service_entity_out_source'] = self.service_entity_out_source.to_alipay_dict()
            else:
                params['service_entity_out_source'] = self.service_entity_out_source
        if self.service_entity_picture:
            if hasattr(self.service_entity_picture, 'to_alipay_dict'):
                params['service_entity_picture'] = self.service_entity_picture.to_alipay_dict()
            else:
                params['service_entity_picture'] = self.service_entity_picture
        if self.service_entity_picture_list:
            if isinstance(self.service_entity_picture_list, list):
                for i in range(0, len(self.service_entity_picture_list)):
                    element = self.service_entity_picture_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_entity_picture_list[i] = element.to_alipay_dict()
            if hasattr(self.service_entity_picture_list, 'to_alipay_dict'):
                params['service_entity_picture_list'] = self.service_entity_picture_list.to_alipay_dict()
            else:
                params['service_entity_picture_list'] = self.service_entity_picture_list
        if self.service_entity_target_url:
            if hasattr(self.service_entity_target_url, 'to_alipay_dict'):
                params['service_entity_target_url'] = self.service_entity_target_url.to_alipay_dict()
            else:
                params['service_entity_target_url'] = self.service_entity_target_url
        if self.service_entity_target_url_snd:
            if hasattr(self.service_entity_target_url_snd, 'to_alipay_dict'):
                params['service_entity_target_url_snd'] = self.service_entity_target_url_snd.to_alipay_dict()
            else:
                params['service_entity_target_url_snd'] = self.service_entity_target_url_snd
        if self.service_entity_type:
            if hasattr(self.service_entity_type, 'to_alipay_dict'):
                params['service_entity_type'] = self.service_entity_type.to_alipay_dict()
            else:
                params['service_entity_type'] = self.service_entity_type
        if self.service_entity_video_list:
            if isinstance(self.service_entity_video_list, list):
                for i in range(0, len(self.service_entity_video_list)):
                    element = self.service_entity_video_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_entity_video_list[i] = element.to_alipay_dict()
            if hasattr(self.service_entity_video_list, 'to_alipay_dict'):
                params['service_entity_video_list'] = self.service_entity_video_list.to_alipay_dict()
            else:
                params['service_entity_video_list'] = self.service_entity_video_list
        if self.service_entity_white_picture:
            if hasattr(self.service_entity_white_picture, 'to_alipay_dict'):
                params['service_entity_white_picture'] = self.service_entity_white_picture.to_alipay_dict()
            else:
                params['service_entity_white_picture'] = self.service_entity_white_picture
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceEntity()
        if 'service_entity_app_id' in d:
            o.service_entity_app_id = d['service_entity_app_id']
        if 'service_entity_app_name' in d:
            o.service_entity_app_name = d['service_entity_app_name']
        if 'service_entity_app_url' in d:
            o.service_entity_app_url = d['service_entity_app_url']
        if 'service_entity_desc' in d:
            o.service_entity_desc = d['service_entity_desc']
        if 'service_entity_landing_page' in d:
            o.service_entity_landing_page = d['service_entity_landing_page']
        if 'service_entity_name' in d:
            o.service_entity_name = d['service_entity_name']
        if 'service_entity_no' in d:
            o.service_entity_no = d['service_entity_no']
        if 'service_entity_out_id' in d:
            o.service_entity_out_id = d['service_entity_out_id']
        if 'service_entity_out_source' in d:
            o.service_entity_out_source = d['service_entity_out_source']
        if 'service_entity_picture' in d:
            o.service_entity_picture = d['service_entity_picture']
        if 'service_entity_picture_list' in d:
            o.service_entity_picture_list = d['service_entity_picture_list']
        if 'service_entity_target_url' in d:
            o.service_entity_target_url = d['service_entity_target_url']
        if 'service_entity_target_url_snd' in d:
            o.service_entity_target_url_snd = d['service_entity_target_url_snd']
        if 'service_entity_type' in d:
            o.service_entity_type = d['service_entity_type']
        if 'service_entity_video_list' in d:
            o.service_entity_video_list = d['service_entity_video_list']
        if 'service_entity_white_picture' in d:
            o.service_entity_white_picture = d['service_entity_white_picture']
        return o


