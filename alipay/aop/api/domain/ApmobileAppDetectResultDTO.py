#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileAppPermissionReportDetailDTO import ApmobileAppPermissionReportDetailDTO
from alipay.aop.api.domain.ApmobileAppPermissionReportIndexDTO import ApmobileAppPermissionReportIndexDTO
from alipay.aop.api.domain.ApmobileAppPermissionReportSdkDTO import ApmobileAppPermissionReportSdkDTO
from alipay.aop.api.domain.ApmobileAppPermissionReportSensitiveApiDTO import ApmobileAppPermissionReportSensitiveApiDTO
from alipay.aop.api.domain.ApmobileAppPermissionReportSensitiveDTO import ApmobileAppPermissionReportSensitiveDTO
from alipay.aop.api.domain.ApmobileAppPermissionReportSummaryDTO import ApmobileAppPermissionReportSummaryDTO


class ApmobileAppDetectResultDTO(object):

    def __init__(self):
        self._app_permission_report_detail_dto = None
        self._app_permission_report_index_dto = None
        self._app_permission_report_sdk_dto = None
        self._app_permission_report_sensitive_api_dto = None
        self._app_permission_report_sensitive_dto = None
        self._app_permission_report_summary_dto = None

    @property
    def app_permission_report_detail_dto(self):
        return self._app_permission_report_detail_dto

    @app_permission_report_detail_dto.setter
    def app_permission_report_detail_dto(self, value):
        if isinstance(value, ApmobileAppPermissionReportDetailDTO):
            self._app_permission_report_detail_dto = value
        else:
            self._app_permission_report_detail_dto = ApmobileAppPermissionReportDetailDTO.from_alipay_dict(value)
    @property
    def app_permission_report_index_dto(self):
        return self._app_permission_report_index_dto

    @app_permission_report_index_dto.setter
    def app_permission_report_index_dto(self, value):
        if isinstance(value, ApmobileAppPermissionReportIndexDTO):
            self._app_permission_report_index_dto = value
        else:
            self._app_permission_report_index_dto = ApmobileAppPermissionReportIndexDTO.from_alipay_dict(value)
    @property
    def app_permission_report_sdk_dto(self):
        return self._app_permission_report_sdk_dto

    @app_permission_report_sdk_dto.setter
    def app_permission_report_sdk_dto(self, value):
        if isinstance(value, ApmobileAppPermissionReportSdkDTO):
            self._app_permission_report_sdk_dto = value
        else:
            self._app_permission_report_sdk_dto = ApmobileAppPermissionReportSdkDTO.from_alipay_dict(value)
    @property
    def app_permission_report_sensitive_api_dto(self):
        return self._app_permission_report_sensitive_api_dto

    @app_permission_report_sensitive_api_dto.setter
    def app_permission_report_sensitive_api_dto(self, value):
        if isinstance(value, ApmobileAppPermissionReportSensitiveApiDTO):
            self._app_permission_report_sensitive_api_dto = value
        else:
            self._app_permission_report_sensitive_api_dto = ApmobileAppPermissionReportSensitiveApiDTO.from_alipay_dict(value)
    @property
    def app_permission_report_sensitive_dto(self):
        return self._app_permission_report_sensitive_dto

    @app_permission_report_sensitive_dto.setter
    def app_permission_report_sensitive_dto(self, value):
        if isinstance(value, ApmobileAppPermissionReportSensitiveDTO):
            self._app_permission_report_sensitive_dto = value
        else:
            self._app_permission_report_sensitive_dto = ApmobileAppPermissionReportSensitiveDTO.from_alipay_dict(value)
    @property
    def app_permission_report_summary_dto(self):
        return self._app_permission_report_summary_dto

    @app_permission_report_summary_dto.setter
    def app_permission_report_summary_dto(self, value):
        if isinstance(value, ApmobileAppPermissionReportSummaryDTO):
            self._app_permission_report_summary_dto = value
        else:
            self._app_permission_report_summary_dto = ApmobileAppPermissionReportSummaryDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.app_permission_report_detail_dto:
            if hasattr(self.app_permission_report_detail_dto, 'to_alipay_dict'):
                params['app_permission_report_detail_dto'] = self.app_permission_report_detail_dto.to_alipay_dict()
            else:
                params['app_permission_report_detail_dto'] = self.app_permission_report_detail_dto
        if self.app_permission_report_index_dto:
            if hasattr(self.app_permission_report_index_dto, 'to_alipay_dict'):
                params['app_permission_report_index_dto'] = self.app_permission_report_index_dto.to_alipay_dict()
            else:
                params['app_permission_report_index_dto'] = self.app_permission_report_index_dto
        if self.app_permission_report_sdk_dto:
            if hasattr(self.app_permission_report_sdk_dto, 'to_alipay_dict'):
                params['app_permission_report_sdk_dto'] = self.app_permission_report_sdk_dto.to_alipay_dict()
            else:
                params['app_permission_report_sdk_dto'] = self.app_permission_report_sdk_dto
        if self.app_permission_report_sensitive_api_dto:
            if hasattr(self.app_permission_report_sensitive_api_dto, 'to_alipay_dict'):
                params['app_permission_report_sensitive_api_dto'] = self.app_permission_report_sensitive_api_dto.to_alipay_dict()
            else:
                params['app_permission_report_sensitive_api_dto'] = self.app_permission_report_sensitive_api_dto
        if self.app_permission_report_sensitive_dto:
            if hasattr(self.app_permission_report_sensitive_dto, 'to_alipay_dict'):
                params['app_permission_report_sensitive_dto'] = self.app_permission_report_sensitive_dto.to_alipay_dict()
            else:
                params['app_permission_report_sensitive_dto'] = self.app_permission_report_sensitive_dto
        if self.app_permission_report_summary_dto:
            if hasattr(self.app_permission_report_summary_dto, 'to_alipay_dict'):
                params['app_permission_report_summary_dto'] = self.app_permission_report_summary_dto.to_alipay_dict()
            else:
                params['app_permission_report_summary_dto'] = self.app_permission_report_summary_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileAppDetectResultDTO()
        if 'app_permission_report_detail_dto' in d:
            o.app_permission_report_detail_dto = d['app_permission_report_detail_dto']
        if 'app_permission_report_index_dto' in d:
            o.app_permission_report_index_dto = d['app_permission_report_index_dto']
        if 'app_permission_report_sdk_dto' in d:
            o.app_permission_report_sdk_dto = d['app_permission_report_sdk_dto']
        if 'app_permission_report_sensitive_api_dto' in d:
            o.app_permission_report_sensitive_api_dto = d['app_permission_report_sensitive_api_dto']
        if 'app_permission_report_sensitive_dto' in d:
            o.app_permission_report_sensitive_dto = d['app_permission_report_sensitive_dto']
        if 'app_permission_report_summary_dto' in d:
            o.app_permission_report_summary_dto = d['app_permission_report_summary_dto']
        return o


