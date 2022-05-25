#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *

from alipay.aop.api.domain.RegionInfo import RegionInfo



class AlipayOpenMiniVersionAuditApplyRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._app_category_ids = None
        self._app_desc = None
        self._app_english_name = None
        self._app_name = None
        self._app_slogan = None
        self._app_version = None
        self._audit_rule = None
        self._auto_online = None
        self._bundle_id = None
        self._license_name = None
        self._license_no = None
        self._license_valid_date = None
        self._memo = None
        self._mini_category_ids = None
        self._region_type = None
        self._service_email = None
        self._service_phone = None
        self._service_region_info = None
        self._speed_up = None
        self._test_accout = None
        self._test_password = None
        self._version_desc = None
        self._app_logo = None
        self._fifth_license_pic = None
        self._fifth_screen_shot = None
        self._first_license_pic = None
        self._first_screen_shot = None
        self._first_special_license_pic = None
        self._fourth_license_pic = None
        self._fourth_screen_shot = None
        self._out_door_pic = None
        self._second_license_pic = None
        self._second_screen_shot = None
        self._second_special_license_pic = None
        self._test_file_name = None
        self._third_license_pic = None
        self._third_screen_shot = None
        self._third_special_license_pic = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

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
    def audit_rule(self):
        return self._audit_rule

    @audit_rule.setter
    def audit_rule(self, value):
        self._audit_rule = value
    @property
    def auto_online(self):
        return self._auto_online

    @auto_online.setter
    def auto_online(self, value):
        self._auto_online = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def license_name(self):
        return self._license_name

    @license_name.setter
    def license_name(self, value):
        self._license_name = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
    @property
    def license_valid_date(self):
        return self._license_valid_date

    @license_valid_date.setter
    def license_valid_date(self, value):
        self._license_valid_date = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def mini_category_ids(self):
        return self._mini_category_ids

    @mini_category_ids.setter
    def mini_category_ids(self, value):
        self._mini_category_ids = value
    @property
    def region_type(self):
        return self._region_type

    @region_type.setter
    def region_type(self, value):
        self._region_type = value
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
    def speed_up(self):
        return self._speed_up

    @speed_up.setter
    def speed_up(self, value):
        self._speed_up = value
    @property
    def test_accout(self):
        return self._test_accout

    @test_accout.setter
    def test_accout(self, value):
        self._test_accout = value
    @property
    def test_password(self):
        return self._test_password

    @test_password.setter
    def test_password(self, value):
        self._test_password = value
    @property
    def version_desc(self):
        return self._version_desc

    @version_desc.setter
    def version_desc(self, value):
        self._version_desc = value

    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        if not isinstance(value, FileItem):
            return
        self._app_logo = value
    @property
    def fifth_license_pic(self):
        return self._fifth_license_pic

    @fifth_license_pic.setter
    def fifth_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._fifth_license_pic = value
    @property
    def fifth_screen_shot(self):
        return self._fifth_screen_shot

    @fifth_screen_shot.setter
    def fifth_screen_shot(self, value):
        if not isinstance(value, FileItem):
            return
        self._fifth_screen_shot = value
    @property
    def first_license_pic(self):
        return self._first_license_pic

    @first_license_pic.setter
    def first_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._first_license_pic = value
    @property
    def first_screen_shot(self):
        return self._first_screen_shot

    @first_screen_shot.setter
    def first_screen_shot(self, value):
        if not isinstance(value, FileItem):
            return
        self._first_screen_shot = value
    @property
    def first_special_license_pic(self):
        return self._first_special_license_pic

    @first_special_license_pic.setter
    def first_special_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._first_special_license_pic = value
    @property
    def fourth_license_pic(self):
        return self._fourth_license_pic

    @fourth_license_pic.setter
    def fourth_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._fourth_license_pic = value
    @property
    def fourth_screen_shot(self):
        return self._fourth_screen_shot

    @fourth_screen_shot.setter
    def fourth_screen_shot(self, value):
        if not isinstance(value, FileItem):
            return
        self._fourth_screen_shot = value
    @property
    def out_door_pic(self):
        return self._out_door_pic

    @out_door_pic.setter
    def out_door_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._out_door_pic = value
    @property
    def second_license_pic(self):
        return self._second_license_pic

    @second_license_pic.setter
    def second_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._second_license_pic = value
    @property
    def second_screen_shot(self):
        return self._second_screen_shot

    @second_screen_shot.setter
    def second_screen_shot(self, value):
        if not isinstance(value, FileItem):
            return
        self._second_screen_shot = value
    @property
    def second_special_license_pic(self):
        return self._second_special_license_pic

    @second_special_license_pic.setter
    def second_special_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._second_special_license_pic = value
    @property
    def test_file_name(self):
        return self._test_file_name

    @test_file_name.setter
    def test_file_name(self, value):
        if not isinstance(value, FileItem):
            return
        self._test_file_name = value
    @property
    def third_license_pic(self):
        return self._third_license_pic

    @third_license_pic.setter
    def third_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._third_license_pic = value
    @property
    def third_screen_shot(self):
        return self._third_screen_shot

    @third_screen_shot.setter
    def third_screen_shot(self, value):
        if not isinstance(value, FileItem):
            return
        self._third_screen_shot = value
    @property
    def third_special_license_pic(self):
        return self._third_special_license_pic

    @third_special_license_pic.setter
    def third_special_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._third_special_license_pic = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.open.mini.version.audit.apply'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.app_category_ids:
            if hasattr(self.app_category_ids, 'to_alipay_dict'):
                params['app_category_ids'] = json.dumps(obj=self.app_category_ids.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['app_category_ids'] = self.app_category_ids
        if self.app_desc:
            if hasattr(self.app_desc, 'to_alipay_dict'):
                params['app_desc'] = json.dumps(obj=self.app_desc.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['app_desc'] = self.app_desc
        if self.app_english_name:
            if hasattr(self.app_english_name, 'to_alipay_dict'):
                params['app_english_name'] = json.dumps(obj=self.app_english_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['app_english_name'] = self.app_english_name
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = json.dumps(obj=self.app_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['app_name'] = self.app_name
        if self.app_slogan:
            if hasattr(self.app_slogan, 'to_alipay_dict'):
                params['app_slogan'] = json.dumps(obj=self.app_slogan.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['app_slogan'] = self.app_slogan
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = json.dumps(obj=self.app_version.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['app_version'] = self.app_version
        if self.audit_rule:
            if hasattr(self.audit_rule, 'to_alipay_dict'):
                params['audit_rule'] = json.dumps(obj=self.audit_rule.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['audit_rule'] = self.audit_rule
        if self.auto_online:
            if hasattr(self.auto_online, 'to_alipay_dict'):
                params['auto_online'] = json.dumps(obj=self.auto_online.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['auto_online'] = self.auto_online
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = json.dumps(obj=self.bundle_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['bundle_id'] = self.bundle_id
        if self.license_name:
            if hasattr(self.license_name, 'to_alipay_dict'):
                params['license_name'] = json.dumps(obj=self.license_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['license_name'] = self.license_name
        if self.license_no:
            if hasattr(self.license_no, 'to_alipay_dict'):
                params['license_no'] = json.dumps(obj=self.license_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['license_no'] = self.license_no
        if self.license_valid_date:
            if hasattr(self.license_valid_date, 'to_alipay_dict'):
                params['license_valid_date'] = json.dumps(obj=self.license_valid_date.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['license_valid_date'] = self.license_valid_date
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = json.dumps(obj=self.memo.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['memo'] = self.memo
        if self.mini_category_ids:
            if hasattr(self.mini_category_ids, 'to_alipay_dict'):
                params['mini_category_ids'] = json.dumps(obj=self.mini_category_ids.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['mini_category_ids'] = self.mini_category_ids
        if self.region_type:
            if hasattr(self.region_type, 'to_alipay_dict'):
                params['region_type'] = json.dumps(obj=self.region_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['region_type'] = self.region_type
        if self.service_email:
            if hasattr(self.service_email, 'to_alipay_dict'):
                params['service_email'] = json.dumps(obj=self.service_email.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['service_email'] = self.service_email
        if self.service_phone:
            if hasattr(self.service_phone, 'to_alipay_dict'):
                params['service_phone'] = json.dumps(obj=self.service_phone.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['service_phone'] = self.service_phone
        if self.service_region_info:
            if isinstance(self.service_region_info, list):
                for i in range(0, len(self.service_region_info)):
                    element = self.service_region_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_region_info[i] = element.to_alipay_dict()
                params['service_region_info'] = json.dumps(obj=self.service_region_info, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.speed_up:
            if hasattr(self.speed_up, 'to_alipay_dict'):
                params['speed_up'] = json.dumps(obj=self.speed_up.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['speed_up'] = self.speed_up
        if self.test_accout:
            if hasattr(self.test_accout, 'to_alipay_dict'):
                params['test_accout'] = json.dumps(obj=self.test_accout.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['test_accout'] = self.test_accout
        if self.test_password:
            if hasattr(self.test_password, 'to_alipay_dict'):
                params['test_password'] = json.dumps(obj=self.test_password.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['test_password'] = self.test_password
        if self.version_desc:
            if hasattr(self.version_desc, 'to_alipay_dict'):
                params['version_desc'] = json.dumps(obj=self.version_desc.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['version_desc'] = self.version_desc
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        if self.app_logo:
            multipart_params['app_logo'] = self.app_logo
        if self.fifth_license_pic:
            multipart_params['fifth_license_pic'] = self.fifth_license_pic
        if self.fifth_screen_shot:
            multipart_params['fifth_screen_shot'] = self.fifth_screen_shot
        if self.first_license_pic:
            multipart_params['first_license_pic'] = self.first_license_pic
        if self.first_screen_shot:
            multipart_params['first_screen_shot'] = self.first_screen_shot
        if self.first_special_license_pic:
            multipart_params['first_special_license_pic'] = self.first_special_license_pic
        if self.fourth_license_pic:
            multipart_params['fourth_license_pic'] = self.fourth_license_pic
        if self.fourth_screen_shot:
            multipart_params['fourth_screen_shot'] = self.fourth_screen_shot
        if self.out_door_pic:
            multipart_params['out_door_pic'] = self.out_door_pic
        if self.second_license_pic:
            multipart_params['second_license_pic'] = self.second_license_pic
        if self.second_screen_shot:
            multipart_params['second_screen_shot'] = self.second_screen_shot
        if self.second_special_license_pic:
            multipart_params['second_special_license_pic'] = self.second_special_license_pic
        if self.test_file_name:
            multipart_params['test_file_name'] = self.test_file_name
        if self.third_license_pic:
            multipart_params['third_license_pic'] = self.third_license_pic
        if self.third_screen_shot:
            multipart_params['third_screen_shot'] = self.third_screen_shot
        if self.third_special_license_pic:
            multipart_params['third_special_license_pic'] = self.third_special_license_pic
        return multipart_params
