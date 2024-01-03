#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PhotoInfo import PhotoInfo
from alipay.aop.api.domain.PhotoInfo import PhotoInfo


class IntlBrandInfo(object):

    def __init__(self):
        self._brand_description = None
        self._brand_logo = None
        self._brand_name = None
        self._brand_version = None
        self._cn_name = None
        self._ext_info = None
        self._id = None
        self._label_names = None
        self._master_photo = None
        self._region = None
        self._video_url = None

    @property
    def brand_description(self):
        return self._brand_description

    @brand_description.setter
    def brand_description(self, value):
        self._brand_description = value
    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        if isinstance(value, PhotoInfo):
            self._brand_logo = value
        else:
            self._brand_logo = PhotoInfo.from_alipay_dict(value)
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def brand_version(self):
        return self._brand_version

    @brand_version.setter
    def brand_version(self, value):
        self._brand_version = value
    @property
    def cn_name(self):
        return self._cn_name

    @cn_name.setter
    def cn_name(self, value):
        self._cn_name = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def label_names(self):
        return self._label_names

    @label_names.setter
    def label_names(self, value):
        if isinstance(value, list):
            self._label_names = list()
            for i in value:
                self._label_names.append(i)
    @property
    def master_photo(self):
        return self._master_photo

    @master_photo.setter
    def master_photo(self, value):
        if isinstance(value, PhotoInfo):
            self._master_photo = value
        else:
            self._master_photo = PhotoInfo.from_alipay_dict(value)
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def video_url(self):
        return self._video_url

    @video_url.setter
    def video_url(self, value):
        self._video_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_description:
            if hasattr(self.brand_description, 'to_alipay_dict'):
                params['brand_description'] = self.brand_description.to_alipay_dict()
            else:
                params['brand_description'] = self.brand_description
        if self.brand_logo:
            if hasattr(self.brand_logo, 'to_alipay_dict'):
                params['brand_logo'] = self.brand_logo.to_alipay_dict()
            else:
                params['brand_logo'] = self.brand_logo
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.brand_version:
            if hasattr(self.brand_version, 'to_alipay_dict'):
                params['brand_version'] = self.brand_version.to_alipay_dict()
            else:
                params['brand_version'] = self.brand_version
        if self.cn_name:
            if hasattr(self.cn_name, 'to_alipay_dict'):
                params['cn_name'] = self.cn_name.to_alipay_dict()
            else:
                params['cn_name'] = self.cn_name
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.label_names:
            if isinstance(self.label_names, list):
                for i in range(0, len(self.label_names)):
                    element = self.label_names[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label_names[i] = element.to_alipay_dict()
            if hasattr(self.label_names, 'to_alipay_dict'):
                params['label_names'] = self.label_names.to_alipay_dict()
            else:
                params['label_names'] = self.label_names
        if self.master_photo:
            if hasattr(self.master_photo, 'to_alipay_dict'):
                params['master_photo'] = self.master_photo.to_alipay_dict()
            else:
                params['master_photo'] = self.master_photo
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.video_url:
            if hasattr(self.video_url, 'to_alipay_dict'):
                params['video_url'] = self.video_url.to_alipay_dict()
            else:
                params['video_url'] = self.video_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IntlBrandInfo()
        if 'brand_description' in d:
            o.brand_description = d['brand_description']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'brand_version' in d:
            o.brand_version = d['brand_version']
        if 'cn_name' in d:
            o.cn_name = d['cn_name']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'id' in d:
            o.id = d['id']
        if 'label_names' in d:
            o.label_names = d['label_names']
        if 'master_photo' in d:
            o.master_photo = d['master_photo']
        if 'region' in d:
            o.region = d['region']
        if 'video_url' in d:
            o.video_url = d['video_url']
        return o


