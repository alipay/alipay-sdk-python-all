#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuditLicenseInfo import AuditLicenseInfo


class AlipayOpenMiniInnerversionBuildauditSubmitModel(object):

    def __init__(self):
        self._app_category_ids = None
        self._app_desc = None
        self._app_english_name = None
        self._app_logo = None
        self._app_name = None
        self._app_origin = None
        self._app_slogan = None
        self._app_version = None
        self._build_ext = None
        self._bundle_id = None
        self._isv_app_id = None
        self._license_info = None
        self._mini_app_id = None
        self._mini_category_ids = None
        self._pid = None
        self._region_type = None
        self._screen_shot_list = None
        self._service_phone = None
        self._special_license_pic_list = None
        self._template_id = None
        self._template_version = None
        self._version_desc = None

    @property
    def app_category_ids(self):
        return self._app_category_ids

    @app_category_ids.setter
    def app_category_ids(self, value):
        self._app_category_ids = value
    @property
    def app_desc(self):
        return self._app_desc

    @app_desc.setter
    def app_desc(self, value):
        self._app_desc = value
    @property
    def app_english_name(self):
        return self._app_english_name

    @app_english_name.setter
    def app_english_name(self, value):
        self._app_english_name = value
    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        self._app_logo = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def app_slogan(self):
        return self._app_slogan

    @app_slogan.setter
    def app_slogan(self, value):
        self._app_slogan = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def build_ext(self):
        return self._build_ext

    @build_ext.setter
    def build_ext(self, value):
        self._build_ext = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def isv_app_id(self):
        return self._isv_app_id

    @isv_app_id.setter
    def isv_app_id(self, value):
        self._isv_app_id = value
    @property
    def license_info(self):
        return self._license_info

    @license_info.setter
    def license_info(self, value):
        if isinstance(value, AuditLicenseInfo):
            self._license_info = value
        else:
            self._license_info = AuditLicenseInfo.from_alipay_dict(value)
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_category_ids(self):
        return self._mini_category_ids

    @mini_category_ids.setter
    def mini_category_ids(self, value):
        self._mini_category_ids = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def region_type(self):
        return self._region_type

    @region_type.setter
    def region_type(self, value):
        self._region_type = value
    @property
    def screen_shot_list(self):
        return self._screen_shot_list

    @screen_shot_list.setter
    def screen_shot_list(self, value):
        self._screen_shot_list = value
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value
    @property
    def special_license_pic_list(self):
        return self._special_license_pic_list

    @special_license_pic_list.setter
    def special_license_pic_list(self, value):
        self._special_license_pic_list = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_version(self):
        return self._template_version

    @template_version.setter
    def template_version(self, value):
        self._template_version = value
    @property
    def version_desc(self):
        return self._version_desc

    @version_desc.setter
    def version_desc(self, value):
        self._version_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_category_ids:
            if hasattr(self.app_category_ids, 'to_alipay_dict'):
                params['app_category_ids'] = self.app_category_ids.to_alipay_dict()
            else:
                params['app_category_ids'] = self.app_category_ids
        if self.app_desc:
            if hasattr(self.app_desc, 'to_alipay_dict'):
                params['app_desc'] = self.app_desc.to_alipay_dict()
            else:
                params['app_desc'] = self.app_desc
        if self.app_english_name:
            if hasattr(self.app_english_name, 'to_alipay_dict'):
                params['app_english_name'] = self.app_english_name.to_alipay_dict()
            else:
                params['app_english_name'] = self.app_english_name
        if self.app_logo:
            if hasattr(self.app_logo, 'to_alipay_dict'):
                params['app_logo'] = self.app_logo.to_alipay_dict()
            else:
                params['app_logo'] = self.app_logo
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.app_slogan:
            if hasattr(self.app_slogan, 'to_alipay_dict'):
                params['app_slogan'] = self.app_slogan.to_alipay_dict()
            else:
                params['app_slogan'] = self.app_slogan
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.build_ext:
            if hasattr(self.build_ext, 'to_alipay_dict'):
                params['build_ext'] = self.build_ext.to_alipay_dict()
            else:
                params['build_ext'] = self.build_ext
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.isv_app_id:
            if hasattr(self.isv_app_id, 'to_alipay_dict'):
                params['isv_app_id'] = self.isv_app_id.to_alipay_dict()
            else:
                params['isv_app_id'] = self.isv_app_id
        if self.license_info:
            if hasattr(self.license_info, 'to_alipay_dict'):
                params['license_info'] = self.license_info.to_alipay_dict()
            else:
                params['license_info'] = self.license_info
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_category_ids:
            if hasattr(self.mini_category_ids, 'to_alipay_dict'):
                params['mini_category_ids'] = self.mini_category_ids.to_alipay_dict()
            else:
                params['mini_category_ids'] = self.mini_category_ids
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.region_type:
            if hasattr(self.region_type, 'to_alipay_dict'):
                params['region_type'] = self.region_type.to_alipay_dict()
            else:
                params['region_type'] = self.region_type
        if self.screen_shot_list:
            if hasattr(self.screen_shot_list, 'to_alipay_dict'):
                params['screen_shot_list'] = self.screen_shot_list.to_alipay_dict()
            else:
                params['screen_shot_list'] = self.screen_shot_list
        if self.service_phone:
            if hasattr(self.service_phone, 'to_alipay_dict'):
                params['service_phone'] = self.service_phone.to_alipay_dict()
            else:
                params['service_phone'] = self.service_phone
        if self.special_license_pic_list:
            if hasattr(self.special_license_pic_list, 'to_alipay_dict'):
                params['special_license_pic_list'] = self.special_license_pic_list.to_alipay_dict()
            else:
                params['special_license_pic_list'] = self.special_license_pic_list
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_version:
            if hasattr(self.template_version, 'to_alipay_dict'):
                params['template_version'] = self.template_version.to_alipay_dict()
            else:
                params['template_version'] = self.template_version
        if self.version_desc:
            if hasattr(self.version_desc, 'to_alipay_dict'):
                params['version_desc'] = self.version_desc.to_alipay_dict()
            else:
                params['version_desc'] = self.version_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerversionBuildauditSubmitModel()
        if 'app_category_ids' in d:
            o.app_category_ids = d['app_category_ids']
        if 'app_desc' in d:
            o.app_desc = d['app_desc']
        if 'app_english_name' in d:
            o.app_english_name = d['app_english_name']
        if 'app_logo' in d:
            o.app_logo = d['app_logo']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'app_slogan' in d:
            o.app_slogan = d['app_slogan']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'build_ext' in d:
            o.build_ext = d['build_ext']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'isv_app_id' in d:
            o.isv_app_id = d['isv_app_id']
        if 'license_info' in d:
            o.license_info = d['license_info']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_category_ids' in d:
            o.mini_category_ids = d['mini_category_ids']
        if 'pid' in d:
            o.pid = d['pid']
        if 'region_type' in d:
            o.region_type = d['region_type']
        if 'screen_shot_list' in d:
            o.screen_shot_list = d['screen_shot_list']
        if 'service_phone' in d:
            o.service_phone = d['service_phone']
        if 'special_license_pic_list' in d:
            o.special_license_pic_list = d['special_license_pic_list']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_version' in d:
            o.template_version = d['template_version']
        if 'version_desc' in d:
            o.version_desc = d['version_desc']
        return o


