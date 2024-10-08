#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentEnterpriseCertification(object):

    def __init__(self):
        self._agent_person_cellphone = None
        self._agent_person_cert_expire_date = None
        self._agent_person_cert_no = None
        self._agent_person_cert_start_date = None
        self._agent_person_emblem_cert_image_url = None
        self._agent_person_face_cert_image_url = None
        self._agent_person_name = None
        self._appid = None
        self._auth_status = None
        self._certification_result = None
        self._certification_type = None
        self._enterprise_address = None
        self._enterprise_license_expire_date = None
        self._enterprise_license_image_url = None
        self._enterprise_license_start_date = None
        self._enterprise_name = None
        self._gmt_authentication_success = None
        self._legal_person_cellphone = None
        self._legal_person_cert_expire_date = None
        self._legal_person_cert_no = None
        self._legal_person_cert_start_date = None
        self._legal_person_emblem_cert_image_url = None
        self._legal_person_face_cert_image_url = None
        self._legal_person_name = None
        self._open_id = None
        self._org_type = None
        self._partner_id = None
        self._partner_open_id = None
        self._unified_social_credit_code = None
        self._user_id = None

    @property
    def agent_person_cellphone(self):
        return self._agent_person_cellphone

    @agent_person_cellphone.setter
    def agent_person_cellphone(self, value):
        self._agent_person_cellphone = value
    @property
    def agent_person_cert_expire_date(self):
        return self._agent_person_cert_expire_date

    @agent_person_cert_expire_date.setter
    def agent_person_cert_expire_date(self, value):
        self._agent_person_cert_expire_date = value
    @property
    def agent_person_cert_no(self):
        return self._agent_person_cert_no

    @agent_person_cert_no.setter
    def agent_person_cert_no(self, value):
        self._agent_person_cert_no = value
    @property
    def agent_person_cert_start_date(self):
        return self._agent_person_cert_start_date

    @agent_person_cert_start_date.setter
    def agent_person_cert_start_date(self, value):
        self._agent_person_cert_start_date = value
    @property
    def agent_person_emblem_cert_image_url(self):
        return self._agent_person_emblem_cert_image_url

    @agent_person_emblem_cert_image_url.setter
    def agent_person_emblem_cert_image_url(self, value):
        self._agent_person_emblem_cert_image_url = value
    @property
    def agent_person_face_cert_image_url(self):
        return self._agent_person_face_cert_image_url

    @agent_person_face_cert_image_url.setter
    def agent_person_face_cert_image_url(self, value):
        self._agent_person_face_cert_image_url = value
    @property
    def agent_person_name(self):
        return self._agent_person_name

    @agent_person_name.setter
    def agent_person_name(self, value):
        self._agent_person_name = value
    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def certification_result(self):
        return self._certification_result

    @certification_result.setter
    def certification_result(self, value):
        self._certification_result = value
    @property
    def certification_type(self):
        return self._certification_type

    @certification_type.setter
    def certification_type(self, value):
        self._certification_type = value
    @property
    def enterprise_address(self):
        return self._enterprise_address

    @enterprise_address.setter
    def enterprise_address(self, value):
        self._enterprise_address = value
    @property
    def enterprise_license_expire_date(self):
        return self._enterprise_license_expire_date

    @enterprise_license_expire_date.setter
    def enterprise_license_expire_date(self, value):
        self._enterprise_license_expire_date = value
    @property
    def enterprise_license_image_url(self):
        return self._enterprise_license_image_url

    @enterprise_license_image_url.setter
    def enterprise_license_image_url(self, value):
        self._enterprise_license_image_url = value
    @property
    def enterprise_license_start_date(self):
        return self._enterprise_license_start_date

    @enterprise_license_start_date.setter
    def enterprise_license_start_date(self, value):
        self._enterprise_license_start_date = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def gmt_authentication_success(self):
        return self._gmt_authentication_success

    @gmt_authentication_success.setter
    def gmt_authentication_success(self, value):
        self._gmt_authentication_success = value
    @property
    def legal_person_cellphone(self):
        return self._legal_person_cellphone

    @legal_person_cellphone.setter
    def legal_person_cellphone(self, value):
        self._legal_person_cellphone = value
    @property
    def legal_person_cert_expire_date(self):
        return self._legal_person_cert_expire_date

    @legal_person_cert_expire_date.setter
    def legal_person_cert_expire_date(self, value):
        self._legal_person_cert_expire_date = value
    @property
    def legal_person_cert_no(self):
        return self._legal_person_cert_no

    @legal_person_cert_no.setter
    def legal_person_cert_no(self, value):
        self._legal_person_cert_no = value
    @property
    def legal_person_cert_start_date(self):
        return self._legal_person_cert_start_date

    @legal_person_cert_start_date.setter
    def legal_person_cert_start_date(self, value):
        self._legal_person_cert_start_date = value
    @property
    def legal_person_emblem_cert_image_url(self):
        return self._legal_person_emblem_cert_image_url

    @legal_person_emblem_cert_image_url.setter
    def legal_person_emblem_cert_image_url(self, value):
        self._legal_person_emblem_cert_image_url = value
    @property
    def legal_person_face_cert_image_url(self):
        return self._legal_person_face_cert_image_url

    @legal_person_face_cert_image_url.setter
    def legal_person_face_cert_image_url(self, value):
        self._legal_person_face_cert_image_url = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def org_type(self):
        return self._org_type

    @org_type.setter
    def org_type(self, value):
        self._org_type = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def partner_open_id(self):
        return self._partner_open_id

    @partner_open_id.setter
    def partner_open_id(self, value):
        self._partner_open_id = value
    @property
    def unified_social_credit_code(self):
        return self._unified_social_credit_code

    @unified_social_credit_code.setter
    def unified_social_credit_code(self, value):
        self._unified_social_credit_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_person_cellphone:
            if hasattr(self.agent_person_cellphone, 'to_alipay_dict'):
                params['agent_person_cellphone'] = self.agent_person_cellphone.to_alipay_dict()
            else:
                params['agent_person_cellphone'] = self.agent_person_cellphone
        if self.agent_person_cert_expire_date:
            if hasattr(self.agent_person_cert_expire_date, 'to_alipay_dict'):
                params['agent_person_cert_expire_date'] = self.agent_person_cert_expire_date.to_alipay_dict()
            else:
                params['agent_person_cert_expire_date'] = self.agent_person_cert_expire_date
        if self.agent_person_cert_no:
            if hasattr(self.agent_person_cert_no, 'to_alipay_dict'):
                params['agent_person_cert_no'] = self.agent_person_cert_no.to_alipay_dict()
            else:
                params['agent_person_cert_no'] = self.agent_person_cert_no
        if self.agent_person_cert_start_date:
            if hasattr(self.agent_person_cert_start_date, 'to_alipay_dict'):
                params['agent_person_cert_start_date'] = self.agent_person_cert_start_date.to_alipay_dict()
            else:
                params['agent_person_cert_start_date'] = self.agent_person_cert_start_date
        if self.agent_person_emblem_cert_image_url:
            if hasattr(self.agent_person_emblem_cert_image_url, 'to_alipay_dict'):
                params['agent_person_emblem_cert_image_url'] = self.agent_person_emblem_cert_image_url.to_alipay_dict()
            else:
                params['agent_person_emblem_cert_image_url'] = self.agent_person_emblem_cert_image_url
        if self.agent_person_face_cert_image_url:
            if hasattr(self.agent_person_face_cert_image_url, 'to_alipay_dict'):
                params['agent_person_face_cert_image_url'] = self.agent_person_face_cert_image_url.to_alipay_dict()
            else:
                params['agent_person_face_cert_image_url'] = self.agent_person_face_cert_image_url
        if self.agent_person_name:
            if hasattr(self.agent_person_name, 'to_alipay_dict'):
                params['agent_person_name'] = self.agent_person_name.to_alipay_dict()
            else:
                params['agent_person_name'] = self.agent_person_name
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.auth_status:
            if hasattr(self.auth_status, 'to_alipay_dict'):
                params['auth_status'] = self.auth_status.to_alipay_dict()
            else:
                params['auth_status'] = self.auth_status
        if self.certification_result:
            if hasattr(self.certification_result, 'to_alipay_dict'):
                params['certification_result'] = self.certification_result.to_alipay_dict()
            else:
                params['certification_result'] = self.certification_result
        if self.certification_type:
            if hasattr(self.certification_type, 'to_alipay_dict'):
                params['certification_type'] = self.certification_type.to_alipay_dict()
            else:
                params['certification_type'] = self.certification_type
        if self.enterprise_address:
            if hasattr(self.enterprise_address, 'to_alipay_dict'):
                params['enterprise_address'] = self.enterprise_address.to_alipay_dict()
            else:
                params['enterprise_address'] = self.enterprise_address
        if self.enterprise_license_expire_date:
            if hasattr(self.enterprise_license_expire_date, 'to_alipay_dict'):
                params['enterprise_license_expire_date'] = self.enterprise_license_expire_date.to_alipay_dict()
            else:
                params['enterprise_license_expire_date'] = self.enterprise_license_expire_date
        if self.enterprise_license_image_url:
            if hasattr(self.enterprise_license_image_url, 'to_alipay_dict'):
                params['enterprise_license_image_url'] = self.enterprise_license_image_url.to_alipay_dict()
            else:
                params['enterprise_license_image_url'] = self.enterprise_license_image_url
        if self.enterprise_license_start_date:
            if hasattr(self.enterprise_license_start_date, 'to_alipay_dict'):
                params['enterprise_license_start_date'] = self.enterprise_license_start_date.to_alipay_dict()
            else:
                params['enterprise_license_start_date'] = self.enterprise_license_start_date
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.gmt_authentication_success:
            if hasattr(self.gmt_authentication_success, 'to_alipay_dict'):
                params['gmt_authentication_success'] = self.gmt_authentication_success.to_alipay_dict()
            else:
                params['gmt_authentication_success'] = self.gmt_authentication_success
        if self.legal_person_cellphone:
            if hasattr(self.legal_person_cellphone, 'to_alipay_dict'):
                params['legal_person_cellphone'] = self.legal_person_cellphone.to_alipay_dict()
            else:
                params['legal_person_cellphone'] = self.legal_person_cellphone
        if self.legal_person_cert_expire_date:
            if hasattr(self.legal_person_cert_expire_date, 'to_alipay_dict'):
                params['legal_person_cert_expire_date'] = self.legal_person_cert_expire_date.to_alipay_dict()
            else:
                params['legal_person_cert_expire_date'] = self.legal_person_cert_expire_date
        if self.legal_person_cert_no:
            if hasattr(self.legal_person_cert_no, 'to_alipay_dict'):
                params['legal_person_cert_no'] = self.legal_person_cert_no.to_alipay_dict()
            else:
                params['legal_person_cert_no'] = self.legal_person_cert_no
        if self.legal_person_cert_start_date:
            if hasattr(self.legal_person_cert_start_date, 'to_alipay_dict'):
                params['legal_person_cert_start_date'] = self.legal_person_cert_start_date.to_alipay_dict()
            else:
                params['legal_person_cert_start_date'] = self.legal_person_cert_start_date
        if self.legal_person_emblem_cert_image_url:
            if hasattr(self.legal_person_emblem_cert_image_url, 'to_alipay_dict'):
                params['legal_person_emblem_cert_image_url'] = self.legal_person_emblem_cert_image_url.to_alipay_dict()
            else:
                params['legal_person_emblem_cert_image_url'] = self.legal_person_emblem_cert_image_url
        if self.legal_person_face_cert_image_url:
            if hasattr(self.legal_person_face_cert_image_url, 'to_alipay_dict'):
                params['legal_person_face_cert_image_url'] = self.legal_person_face_cert_image_url.to_alipay_dict()
            else:
                params['legal_person_face_cert_image_url'] = self.legal_person_face_cert_image_url
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.org_type:
            if hasattr(self.org_type, 'to_alipay_dict'):
                params['org_type'] = self.org_type.to_alipay_dict()
            else:
                params['org_type'] = self.org_type
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.partner_open_id:
            if hasattr(self.partner_open_id, 'to_alipay_dict'):
                params['partner_open_id'] = self.partner_open_id.to_alipay_dict()
            else:
                params['partner_open_id'] = self.partner_open_id
        if self.unified_social_credit_code:
            if hasattr(self.unified_social_credit_code, 'to_alipay_dict'):
                params['unified_social_credit_code'] = self.unified_social_credit_code.to_alipay_dict()
            else:
                params['unified_social_credit_code'] = self.unified_social_credit_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentEnterpriseCertification()
        if 'agent_person_cellphone' in d:
            o.agent_person_cellphone = d['agent_person_cellphone']
        if 'agent_person_cert_expire_date' in d:
            o.agent_person_cert_expire_date = d['agent_person_cert_expire_date']
        if 'agent_person_cert_no' in d:
            o.agent_person_cert_no = d['agent_person_cert_no']
        if 'agent_person_cert_start_date' in d:
            o.agent_person_cert_start_date = d['agent_person_cert_start_date']
        if 'agent_person_emblem_cert_image_url' in d:
            o.agent_person_emblem_cert_image_url = d['agent_person_emblem_cert_image_url']
        if 'agent_person_face_cert_image_url' in d:
            o.agent_person_face_cert_image_url = d['agent_person_face_cert_image_url']
        if 'agent_person_name' in d:
            o.agent_person_name = d['agent_person_name']
        if 'appid' in d:
            o.appid = d['appid']
        if 'auth_status' in d:
            o.auth_status = d['auth_status']
        if 'certification_result' in d:
            o.certification_result = d['certification_result']
        if 'certification_type' in d:
            o.certification_type = d['certification_type']
        if 'enterprise_address' in d:
            o.enterprise_address = d['enterprise_address']
        if 'enterprise_license_expire_date' in d:
            o.enterprise_license_expire_date = d['enterprise_license_expire_date']
        if 'enterprise_license_image_url' in d:
            o.enterprise_license_image_url = d['enterprise_license_image_url']
        if 'enterprise_license_start_date' in d:
            o.enterprise_license_start_date = d['enterprise_license_start_date']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'gmt_authentication_success' in d:
            o.gmt_authentication_success = d['gmt_authentication_success']
        if 'legal_person_cellphone' in d:
            o.legal_person_cellphone = d['legal_person_cellphone']
        if 'legal_person_cert_expire_date' in d:
            o.legal_person_cert_expire_date = d['legal_person_cert_expire_date']
        if 'legal_person_cert_no' in d:
            o.legal_person_cert_no = d['legal_person_cert_no']
        if 'legal_person_cert_start_date' in d:
            o.legal_person_cert_start_date = d['legal_person_cert_start_date']
        if 'legal_person_emblem_cert_image_url' in d:
            o.legal_person_emblem_cert_image_url = d['legal_person_emblem_cert_image_url']
        if 'legal_person_face_cert_image_url' in d:
            o.legal_person_face_cert_image_url = d['legal_person_face_cert_image_url']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_type' in d:
            o.org_type = d['org_type']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'partner_open_id' in d:
            o.partner_open_id = d['partner_open_id']
        if 'unified_social_credit_code' in d:
            o.unified_social_credit_code = d['unified_social_credit_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


