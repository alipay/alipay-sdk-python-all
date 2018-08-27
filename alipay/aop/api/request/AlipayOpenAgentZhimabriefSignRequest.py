#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *

from alipay.aop.api.domain.ContactModel import ContactModel
from alipay.aop.api.domain.ContactModel import ContactModel
from alipay.aop.api.domain.ContactModel import ContactModel



class AlipayOpenAgentZhimabriefSignRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._alipay_life_name = None
        self._app_name = None
        self._batch_no = None
        self._business_license_no = None
        self._custom_usage_scene = None
        self._date_limitation = None
        self._dr_contact = None
        self._enterprise_alias = None
        self._long_term = None
        self._mcc_code = None
        self._oh_contact = None
        self._pr_contact = None
        self._usage_scene = None
        self._web_sites = None
        self._wechat_official_account_name = None
        self._app_demo = None
        self._business_license_auth_pic = None
        self._business_license_pic = None
        self._enterprise_logo = None
        self._special_license_pic = None
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
    def alipay_life_name(self):
        return self._alipay_life_name

    @alipay_life_name.setter
    def alipay_life_name(self, value):
        self._alipay_life_name = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def business_license_no(self):
        return self._business_license_no

    @business_license_no.setter
    def business_license_no(self, value):
        self._business_license_no = value
    @property
    def custom_usage_scene(self):
        return self._custom_usage_scene

    @custom_usage_scene.setter
    def custom_usage_scene(self, value):
        self._custom_usage_scene = value
    @property
    def date_limitation(self):
        return self._date_limitation

    @date_limitation.setter
    def date_limitation(self, value):
        self._date_limitation = value
    @property
    def dr_contact(self):
        return self._dr_contact

    @dr_contact.setter
    def dr_contact(self, value):
        if isinstance(value, ContactModel):
            self._dr_contact = value
        else:
            self._dr_contact = ContactModel.from_alipay_dict(value)
    @property
    def enterprise_alias(self):
        return self._enterprise_alias

    @enterprise_alias.setter
    def enterprise_alias(self, value):
        self._enterprise_alias = value
    @property
    def long_term(self):
        return self._long_term

    @long_term.setter
    def long_term(self, value):
        self._long_term = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def oh_contact(self):
        return self._oh_contact

    @oh_contact.setter
    def oh_contact(self, value):
        if isinstance(value, ContactModel):
            self._oh_contact = value
        else:
            self._oh_contact = ContactModel.from_alipay_dict(value)
    @property
    def pr_contact(self):
        return self._pr_contact

    @pr_contact.setter
    def pr_contact(self, value):
        if isinstance(value, ContactModel):
            self._pr_contact = value
        else:
            self._pr_contact = ContactModel.from_alipay_dict(value)
    @property
    def usage_scene(self):
        return self._usage_scene

    @usage_scene.setter
    def usage_scene(self, value):
        if isinstance(value, list):
            self._usage_scene = list()
            for i in value:
                self._usage_scene.append(i)
    @property
    def web_sites(self):
        return self._web_sites

    @web_sites.setter
    def web_sites(self, value):
        if isinstance(value, list):
            self._web_sites = list()
            for i in value:
                self._web_sites.append(i)
    @property
    def wechat_official_account_name(self):
        return self._wechat_official_account_name

    @wechat_official_account_name.setter
    def wechat_official_account_name(self, value):
        self._wechat_official_account_name = value

    @property
    def app_demo(self):
        return self._app_demo

    @app_demo.setter
    def app_demo(self, value):
        if not isinstance(value, FileItem):
            return
        self._app_demo = value
    @property
    def business_license_auth_pic(self):
        return self._business_license_auth_pic

    @business_license_auth_pic.setter
    def business_license_auth_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._business_license_auth_pic = value
    @property
    def business_license_pic(self):
        return self._business_license_pic

    @business_license_pic.setter
    def business_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._business_license_pic = value
    @property
    def enterprise_logo(self):
        return self._enterprise_logo

    @enterprise_logo.setter
    def enterprise_logo(self, value):
        if not isinstance(value, FileItem):
            return
        self._enterprise_logo = value
    @property
    def special_license_pic(self):
        return self._special_license_pic

    @special_license_pic.setter
    def special_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._special_license_pic = value

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
        params[P_METHOD] = 'alipay.open.agent.zhimabrief.sign'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.alipay_life_name:
            if hasattr(self.alipay_life_name, 'to_alipay_dict'):
                params['alipay_life_name'] = json.dumps(obj=self.alipay_life_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['alipay_life_name'] = self.alipay_life_name
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = json.dumps(obj=self.app_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['app_name'] = self.app_name
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = json.dumps(obj=self.batch_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['batch_no'] = self.batch_no
        if self.business_license_no:
            if hasattr(self.business_license_no, 'to_alipay_dict'):
                params['business_license_no'] = json.dumps(obj=self.business_license_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['business_license_no'] = self.business_license_no
        if self.custom_usage_scene:
            if hasattr(self.custom_usage_scene, 'to_alipay_dict'):
                params['custom_usage_scene'] = json.dumps(obj=self.custom_usage_scene.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['custom_usage_scene'] = self.custom_usage_scene
        if self.date_limitation:
            if hasattr(self.date_limitation, 'to_alipay_dict'):
                params['date_limitation'] = json.dumps(obj=self.date_limitation.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['date_limitation'] = self.date_limitation
        if self.dr_contact:
            if hasattr(self.dr_contact, 'to_alipay_dict'):
                params['dr_contact'] = json.dumps(obj=self.dr_contact.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['dr_contact'] = self.dr_contact
        if self.enterprise_alias:
            if hasattr(self.enterprise_alias, 'to_alipay_dict'):
                params['enterprise_alias'] = json.dumps(obj=self.enterprise_alias.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['enterprise_alias'] = self.enterprise_alias
        if self.long_term:
            if hasattr(self.long_term, 'to_alipay_dict'):
                params['long_term'] = json.dumps(obj=self.long_term.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['long_term'] = self.long_term
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = json.dumps(obj=self.mcc_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['mcc_code'] = self.mcc_code
        if self.oh_contact:
            if hasattr(self.oh_contact, 'to_alipay_dict'):
                params['oh_contact'] = json.dumps(obj=self.oh_contact.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['oh_contact'] = self.oh_contact
        if self.pr_contact:
            if hasattr(self.pr_contact, 'to_alipay_dict'):
                params['pr_contact'] = json.dumps(obj=self.pr_contact.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['pr_contact'] = self.pr_contact
        if self.usage_scene:
            if isinstance(self.usage_scene, list):
                for i in range(0, len(self.usage_scene)):
                    element = self.usage_scene[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.usage_scene[i] = element.to_alipay_dict()
                params['usage_scene'] = json.dumps(obj=self.usage_scene, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.web_sites:
            if isinstance(self.web_sites, list):
                for i in range(0, len(self.web_sites)):
                    element = self.web_sites[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.web_sites[i] = element.to_alipay_dict()
                params['web_sites'] = json.dumps(obj=self.web_sites, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.wechat_official_account_name:
            if hasattr(self.wechat_official_account_name, 'to_alipay_dict'):
                params['wechat_official_account_name'] = json.dumps(obj=self.wechat_official_account_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['wechat_official_account_name'] = self.wechat_official_account_name
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
        if self.app_demo:
            multipart_params['app_demo'] = self.app_demo
        if self.business_license_auth_pic:
            multipart_params['business_license_auth_pic'] = self.business_license_auth_pic
        if self.business_license_pic:
            multipart_params['business_license_pic'] = self.business_license_pic
        if self.enterprise_logo:
            multipart_params['enterprise_logo'] = self.enterprise_logo
        if self.special_license_pic:
            multipart_params['special_license_pic'] = self.special_license_pic
        return multipart_params
