#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IterationVersionInfoDeliverObj(object):

    def __init__(self):
        self._acceptance_use_case = None
        self._actual_release_time = None
        self._aone_linke = None
        self._deploy_type = None
        self._development_guide = None
        self._else_info = None
        self._eom = None
        self._eos = None
        self._functional_test_report = None
        self._id = None
        self._key_needs = None
        self._l_2 = None
        self._l_3 = None
        self._l_3_code = None
        self._multiplatform = None
        self._performance_test_report = None
        self._product_white_paper = None
        self._release_note = None
        self._security_white_paper = None
        self._stamp_time = None
        self._sys_design_specification = None
        self._sys_installation_and_deployment_manual = None
        self._sys_installation_package = None
        self._sys_operation_and_maintenance_manual = None
        self._tech_white_paper = None
        self._user_manual = None
        self._version_download = None
        self._version_num = None
        self._version_status = None
        self._version_type = None

    @property
    def acceptance_use_case(self):
        return self._acceptance_use_case

    @acceptance_use_case.setter
    def acceptance_use_case(self, value):
        self._acceptance_use_case = value
    @property
    def actual_release_time(self):
        return self._actual_release_time

    @actual_release_time.setter
    def actual_release_time(self, value):
        self._actual_release_time = value
    @property
    def aone_linke(self):
        return self._aone_linke

    @aone_linke.setter
    def aone_linke(self, value):
        self._aone_linke = value
    @property
    def deploy_type(self):
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, value):
        self._deploy_type = value
    @property
    def development_guide(self):
        return self._development_guide

    @development_guide.setter
    def development_guide(self, value):
        self._development_guide = value
    @property
    def else_info(self):
        return self._else_info

    @else_info.setter
    def else_info(self, value):
        self._else_info = value
    @property
    def eom(self):
        return self._eom

    @eom.setter
    def eom(self, value):
        self._eom = value
    @property
    def eos(self):
        return self._eos

    @eos.setter
    def eos(self, value):
        self._eos = value
    @property
    def functional_test_report(self):
        return self._functional_test_report

    @functional_test_report.setter
    def functional_test_report(self, value):
        self._functional_test_report = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def key_needs(self):
        return self._key_needs

    @key_needs.setter
    def key_needs(self, value):
        self._key_needs = value
    @property
    def l_2(self):
        return self._l_2

    @l_2.setter
    def l_2(self, value):
        self._l_2 = value
    @property
    def l_3(self):
        return self._l_3

    @l_3.setter
    def l_3(self, value):
        self._l_3 = value
    @property
    def l_3_code(self):
        return self._l_3_code

    @l_3_code.setter
    def l_3_code(self, value):
        self._l_3_code = value
    @property
    def multiplatform(self):
        return self._multiplatform

    @multiplatform.setter
    def multiplatform(self, value):
        self._multiplatform = value
    @property
    def performance_test_report(self):
        return self._performance_test_report

    @performance_test_report.setter
    def performance_test_report(self, value):
        self._performance_test_report = value
    @property
    def product_white_paper(self):
        return self._product_white_paper

    @product_white_paper.setter
    def product_white_paper(self, value):
        self._product_white_paper = value
    @property
    def release_note(self):
        return self._release_note

    @release_note.setter
    def release_note(self, value):
        self._release_note = value
    @property
    def security_white_paper(self):
        return self._security_white_paper

    @security_white_paper.setter
    def security_white_paper(self, value):
        self._security_white_paper = value
    @property
    def stamp_time(self):
        return self._stamp_time

    @stamp_time.setter
    def stamp_time(self, value):
        self._stamp_time = value
    @property
    def sys_design_specification(self):
        return self._sys_design_specification

    @sys_design_specification.setter
    def sys_design_specification(self, value):
        self._sys_design_specification = value
    @property
    def sys_installation_and_deployment_manual(self):
        return self._sys_installation_and_deployment_manual

    @sys_installation_and_deployment_manual.setter
    def sys_installation_and_deployment_manual(self, value):
        self._sys_installation_and_deployment_manual = value
    @property
    def sys_installation_package(self):
        return self._sys_installation_package

    @sys_installation_package.setter
    def sys_installation_package(self, value):
        self._sys_installation_package = value
    @property
    def sys_operation_and_maintenance_manual(self):
        return self._sys_operation_and_maintenance_manual

    @sys_operation_and_maintenance_manual.setter
    def sys_operation_and_maintenance_manual(self, value):
        self._sys_operation_and_maintenance_manual = value
    @property
    def tech_white_paper(self):
        return self._tech_white_paper

    @tech_white_paper.setter
    def tech_white_paper(self, value):
        self._tech_white_paper = value
    @property
    def user_manual(self):
        return self._user_manual

    @user_manual.setter
    def user_manual(self, value):
        self._user_manual = value
    @property
    def version_download(self):
        return self._version_download

    @version_download.setter
    def version_download(self, value):
        self._version_download = value
    @property
    def version_num(self):
        return self._version_num

    @version_num.setter
    def version_num(self, value):
        self._version_num = value
    @property
    def version_status(self):
        return self._version_status

    @version_status.setter
    def version_status(self, value):
        self._version_status = value
    @property
    def version_type(self):
        return self._version_type

    @version_type.setter
    def version_type(self, value):
        self._version_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.acceptance_use_case:
            if hasattr(self.acceptance_use_case, 'to_alipay_dict'):
                params['acceptance_use_case'] = self.acceptance_use_case.to_alipay_dict()
            else:
                params['acceptance_use_case'] = self.acceptance_use_case
        if self.actual_release_time:
            if hasattr(self.actual_release_time, 'to_alipay_dict'):
                params['actual_release_time'] = self.actual_release_time.to_alipay_dict()
            else:
                params['actual_release_time'] = self.actual_release_time
        if self.aone_linke:
            if hasattr(self.aone_linke, 'to_alipay_dict'):
                params['aone_linke'] = self.aone_linke.to_alipay_dict()
            else:
                params['aone_linke'] = self.aone_linke
        if self.deploy_type:
            if hasattr(self.deploy_type, 'to_alipay_dict'):
                params['deploy_type'] = self.deploy_type.to_alipay_dict()
            else:
                params['deploy_type'] = self.deploy_type
        if self.development_guide:
            if hasattr(self.development_guide, 'to_alipay_dict'):
                params['development_guide'] = self.development_guide.to_alipay_dict()
            else:
                params['development_guide'] = self.development_guide
        if self.else_info:
            if hasattr(self.else_info, 'to_alipay_dict'):
                params['else_info'] = self.else_info.to_alipay_dict()
            else:
                params['else_info'] = self.else_info
        if self.eom:
            if hasattr(self.eom, 'to_alipay_dict'):
                params['eom'] = self.eom.to_alipay_dict()
            else:
                params['eom'] = self.eom
        if self.eos:
            if hasattr(self.eos, 'to_alipay_dict'):
                params['eos'] = self.eos.to_alipay_dict()
            else:
                params['eos'] = self.eos
        if self.functional_test_report:
            if hasattr(self.functional_test_report, 'to_alipay_dict'):
                params['functional_test_report'] = self.functional_test_report.to_alipay_dict()
            else:
                params['functional_test_report'] = self.functional_test_report
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.key_needs:
            if hasattr(self.key_needs, 'to_alipay_dict'):
                params['key_needs'] = self.key_needs.to_alipay_dict()
            else:
                params['key_needs'] = self.key_needs
        if self.l_2:
            if hasattr(self.l_2, 'to_alipay_dict'):
                params['l_2'] = self.l_2.to_alipay_dict()
            else:
                params['l_2'] = self.l_2
        if self.l_3:
            if hasattr(self.l_3, 'to_alipay_dict'):
                params['l_3'] = self.l_3.to_alipay_dict()
            else:
                params['l_3'] = self.l_3
        if self.l_3_code:
            if hasattr(self.l_3_code, 'to_alipay_dict'):
                params['l_3_code'] = self.l_3_code.to_alipay_dict()
            else:
                params['l_3_code'] = self.l_3_code
        if self.multiplatform:
            if hasattr(self.multiplatform, 'to_alipay_dict'):
                params['multiplatform'] = self.multiplatform.to_alipay_dict()
            else:
                params['multiplatform'] = self.multiplatform
        if self.performance_test_report:
            if hasattr(self.performance_test_report, 'to_alipay_dict'):
                params['performance_test_report'] = self.performance_test_report.to_alipay_dict()
            else:
                params['performance_test_report'] = self.performance_test_report
        if self.product_white_paper:
            if hasattr(self.product_white_paper, 'to_alipay_dict'):
                params['product_white_paper'] = self.product_white_paper.to_alipay_dict()
            else:
                params['product_white_paper'] = self.product_white_paper
        if self.release_note:
            if hasattr(self.release_note, 'to_alipay_dict'):
                params['release_note'] = self.release_note.to_alipay_dict()
            else:
                params['release_note'] = self.release_note
        if self.security_white_paper:
            if hasattr(self.security_white_paper, 'to_alipay_dict'):
                params['security_white_paper'] = self.security_white_paper.to_alipay_dict()
            else:
                params['security_white_paper'] = self.security_white_paper
        if self.stamp_time:
            if hasattr(self.stamp_time, 'to_alipay_dict'):
                params['stamp_time'] = self.stamp_time.to_alipay_dict()
            else:
                params['stamp_time'] = self.stamp_time
        if self.sys_design_specification:
            if hasattr(self.sys_design_specification, 'to_alipay_dict'):
                params['sys_design_specification'] = self.sys_design_specification.to_alipay_dict()
            else:
                params['sys_design_specification'] = self.sys_design_specification
        if self.sys_installation_and_deployment_manual:
            if hasattr(self.sys_installation_and_deployment_manual, 'to_alipay_dict'):
                params['sys_installation_and_deployment_manual'] = self.sys_installation_and_deployment_manual.to_alipay_dict()
            else:
                params['sys_installation_and_deployment_manual'] = self.sys_installation_and_deployment_manual
        if self.sys_installation_package:
            if hasattr(self.sys_installation_package, 'to_alipay_dict'):
                params['sys_installation_package'] = self.sys_installation_package.to_alipay_dict()
            else:
                params['sys_installation_package'] = self.sys_installation_package
        if self.sys_operation_and_maintenance_manual:
            if hasattr(self.sys_operation_and_maintenance_manual, 'to_alipay_dict'):
                params['sys_operation_and_maintenance_manual'] = self.sys_operation_and_maintenance_manual.to_alipay_dict()
            else:
                params['sys_operation_and_maintenance_manual'] = self.sys_operation_and_maintenance_manual
        if self.tech_white_paper:
            if hasattr(self.tech_white_paper, 'to_alipay_dict'):
                params['tech_white_paper'] = self.tech_white_paper.to_alipay_dict()
            else:
                params['tech_white_paper'] = self.tech_white_paper
        if self.user_manual:
            if hasattr(self.user_manual, 'to_alipay_dict'):
                params['user_manual'] = self.user_manual.to_alipay_dict()
            else:
                params['user_manual'] = self.user_manual
        if self.version_download:
            if hasattr(self.version_download, 'to_alipay_dict'):
                params['version_download'] = self.version_download.to_alipay_dict()
            else:
                params['version_download'] = self.version_download
        if self.version_num:
            if hasattr(self.version_num, 'to_alipay_dict'):
                params['version_num'] = self.version_num.to_alipay_dict()
            else:
                params['version_num'] = self.version_num
        if self.version_status:
            if hasattr(self.version_status, 'to_alipay_dict'):
                params['version_status'] = self.version_status.to_alipay_dict()
            else:
                params['version_status'] = self.version_status
        if self.version_type:
            if hasattr(self.version_type, 'to_alipay_dict'):
                params['version_type'] = self.version_type.to_alipay_dict()
            else:
                params['version_type'] = self.version_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IterationVersionInfoDeliverObj()
        if 'acceptance_use_case' in d:
            o.acceptance_use_case = d['acceptance_use_case']
        if 'actual_release_time' in d:
            o.actual_release_time = d['actual_release_time']
        if 'aone_linke' in d:
            o.aone_linke = d['aone_linke']
        if 'deploy_type' in d:
            o.deploy_type = d['deploy_type']
        if 'development_guide' in d:
            o.development_guide = d['development_guide']
        if 'else_info' in d:
            o.else_info = d['else_info']
        if 'eom' in d:
            o.eom = d['eom']
        if 'eos' in d:
            o.eos = d['eos']
        if 'functional_test_report' in d:
            o.functional_test_report = d['functional_test_report']
        if 'id' in d:
            o.id = d['id']
        if 'key_needs' in d:
            o.key_needs = d['key_needs']
        if 'l_2' in d:
            o.l_2 = d['l_2']
        if 'l_3' in d:
            o.l_3 = d['l_3']
        if 'l_3_code' in d:
            o.l_3_code = d['l_3_code']
        if 'multiplatform' in d:
            o.multiplatform = d['multiplatform']
        if 'performance_test_report' in d:
            o.performance_test_report = d['performance_test_report']
        if 'product_white_paper' in d:
            o.product_white_paper = d['product_white_paper']
        if 'release_note' in d:
            o.release_note = d['release_note']
        if 'security_white_paper' in d:
            o.security_white_paper = d['security_white_paper']
        if 'stamp_time' in d:
            o.stamp_time = d['stamp_time']
        if 'sys_design_specification' in d:
            o.sys_design_specification = d['sys_design_specification']
        if 'sys_installation_and_deployment_manual' in d:
            o.sys_installation_and_deployment_manual = d['sys_installation_and_deployment_manual']
        if 'sys_installation_package' in d:
            o.sys_installation_package = d['sys_installation_package']
        if 'sys_operation_and_maintenance_manual' in d:
            o.sys_operation_and_maintenance_manual = d['sys_operation_and_maintenance_manual']
        if 'tech_white_paper' in d:
            o.tech_white_paper = d['tech_white_paper']
        if 'user_manual' in d:
            o.user_manual = d['user_manual']
        if 'version_download' in d:
            o.version_download = d['version_download']
        if 'version_num' in d:
            o.version_num = d['version_num']
        if 'version_status' in d:
            o.version_status = d['version_status']
        if 'version_type' in d:
            o.version_type = d['version_type']
        return o


