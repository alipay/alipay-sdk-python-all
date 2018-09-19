#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppCategoryInfo import MiniAppCategoryInfo
from alipay.aop.api.domain.MiniPackageInfo import MiniPackageInfo
from alipay.aop.api.domain.RegionInfo import RegionInfo


class AlipayOpenMiniVersionDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniVersionDetailQueryResponse, self).__init__()
        self._app_desc = None
        self._app_english_name = None
        self._app_logo = None
        self._app_name = None
        self._app_slogan = None
        self._app_version = None
        self._gmt_apply_audit = None
        self._gmt_audit_end = None
        self._gmt_create = None
        self._gmt_offline = None
        self._gmt_online = None
        self._gray_strategy = None
        self._memo = None
        self._mini_app_category_info_list = None
        self._package_info_list = None
        self._reject_reason = None
        self._scan_result = None
        self._screen_shot_list = None
        self._service_email = None
        self._service_phone = None
        self._service_region_info = None
        self._service_region_type = None
        self._status = None
        self._version_desc = None

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
    def gmt_apply_audit(self):
        return self._gmt_apply_audit

    @gmt_apply_audit.setter
    def gmt_apply_audit(self, value):
        self._gmt_apply_audit = value
    @property
    def gmt_audit_end(self):
        return self._gmt_audit_end

    @gmt_audit_end.setter
    def gmt_audit_end(self, value):
        self._gmt_audit_end = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_offline(self):
        return self._gmt_offline

    @gmt_offline.setter
    def gmt_offline(self, value):
        self._gmt_offline = value
    @property
    def gmt_online(self):
        return self._gmt_online

    @gmt_online.setter
    def gmt_online(self, value):
        self._gmt_online = value
    @property
    def gray_strategy(self):
        return self._gray_strategy

    @gray_strategy.setter
    def gray_strategy(self, value):
        self._gray_strategy = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def mini_app_category_info_list(self):
        return self._mini_app_category_info_list

    @mini_app_category_info_list.setter
    def mini_app_category_info_list(self, value):
        if isinstance(value, list):
            self._mini_app_category_info_list = list()
            for i in value:
                if isinstance(i, MiniAppCategoryInfo):
                    self._mini_app_category_info_list.append(i)
                else:
                    self._mini_app_category_info_list.append(MiniAppCategoryInfo.from_alipay_dict(i))
    @property
    def package_info_list(self):
        return self._package_info_list

    @package_info_list.setter
    def package_info_list(self, value):
        if isinstance(value, list):
            self._package_info_list = list()
            for i in value:
                if isinstance(i, MiniPackageInfo):
                    self._package_info_list.append(i)
                else:
                    self._package_info_list.append(MiniPackageInfo.from_alipay_dict(i))
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def scan_result(self):
        return self._scan_result

    @scan_result.setter
    def scan_result(self, value):
        self._scan_result = value
    @property
    def screen_shot_list(self):
        return self._screen_shot_list

    @screen_shot_list.setter
    def screen_shot_list(self, value):
        if isinstance(value, list):
            self._screen_shot_list = list()
            for i in value:
                self._screen_shot_list.append(i)
    @property
    def service_email(self):
        return self._service_email

    @service_email.setter
    def service_email(self, value):
        self._service_email = value
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value
    @property
    def service_region_info(self):
        return self._service_region_info

    @service_region_info.setter
    def service_region_info(self, value):
        if isinstance(value, list):
            self._service_region_info = list()
            for i in value:
                if isinstance(i, RegionInfo):
                    self._service_region_info.append(i)
                else:
                    self._service_region_info.append(RegionInfo.from_alipay_dict(i))
    @property
    def service_region_type(self):
        return self._service_region_type

    @service_region_type.setter
    def service_region_type(self, value):
        self._service_region_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def version_desc(self):
        return self._version_desc

    @version_desc.setter
    def version_desc(self, value):
        self._version_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniVersionDetailQueryResponse, self).parse_response_content(response_content)
        if 'app_desc' in response:
            self.app_desc = response['app_desc']
        if 'app_english_name' in response:
            self.app_english_name = response['app_english_name']
        if 'app_logo' in response:
            self.app_logo = response['app_logo']
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'app_slogan' in response:
            self.app_slogan = response['app_slogan']
        if 'app_version' in response:
            self.app_version = response['app_version']
        if 'gmt_apply_audit' in response:
            self.gmt_apply_audit = response['gmt_apply_audit']
        if 'gmt_audit_end' in response:
            self.gmt_audit_end = response['gmt_audit_end']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_offline' in response:
            self.gmt_offline = response['gmt_offline']
        if 'gmt_online' in response:
            self.gmt_online = response['gmt_online']
        if 'gray_strategy' in response:
            self.gray_strategy = response['gray_strategy']
        if 'memo' in response:
            self.memo = response['memo']
        if 'mini_app_category_info_list' in response:
            self.mini_app_category_info_list = response['mini_app_category_info_list']
        if 'package_info_list' in response:
            self.package_info_list = response['package_info_list']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
        if 'scan_result' in response:
            self.scan_result = response['scan_result']
        if 'screen_shot_list' in response:
            self.screen_shot_list = response['screen_shot_list']
        if 'service_email' in response:
            self.service_email = response['service_email']
        if 'service_phone' in response:
            self.service_phone = response['service_phone']
        if 'service_region_info' in response:
            self.service_region_info = response['service_region_info']
        if 'service_region_type' in response:
            self.service_region_type = response['service_region_type']
        if 'status' in response:
            self.status = response['status']
        if 'version_desc' in response:
            self.version_desc = response['version_desc']
