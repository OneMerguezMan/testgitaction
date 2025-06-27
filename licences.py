# Fichier avec Violations de Licences pour Test de Détection
# ⚠️ ATTENTION: Ce fichier contient des problèmes de licences pour des fins de test uniquement

# Vulnérabilité 1: Utilisation de code GPL v3 dans un projet propriétaire
# Ce code utilise des bibliothèques GPL v3 qui forcent l'ouverture du code source
import gpl_library  # GPL v3 - Force l'ouverture du code source
import proprietary_module  # Code propriétaire fermé

def gpl_function():
    """Fonction utilisant du code GPL v3"""
    result = gpl_library.process_data()
    return proprietary_module.encrypt(result)  # Violation: Code propriétaire avec GPL

# Vulnérabilité 2: Utilisation de code AGPL dans une application SaaS
# AGPL force l'ouverture du code source même pour les utilisateurs réseau
import agpl_database  # AGPL v3 - Force l'ouverture même pour usage réseau
import saas_backend  # Application SaaS propriétaire

def saas_function():
    """Fonction SaaS utilisant du code AGPL"""
    data = agpl_database.query()  # Violation: AGPL dans SaaS
    return saas_backend.process(data)

# Vulnérabilité 3: Utilisation de code LGPL sans respect des conditions
# LGPL permet l'utilisation dans du code propriétaire mais avec conditions
import lgpl_library  # LGPL v2.1 - Permet usage propriétaire avec conditions
import closed_source_app  # Application fermée

def lgpl_violation():
    """Violation des conditions LGPL"""
    # Violation: Modification de la bibliothèque LGPL sans redistribution
    modified_lgpl = lgpl_library.modify_and_use()
    return closed_source_app.use_modified(modified_lgpl)

# Vulnérabilité 4: Utilisation de code MPL sans respect des conditions
# MPL nécessite que les modifications soient sous licence MPL
import mpl_component  # MPL 2.0 - Modifications doivent rester MPL
import proprietary_enhancement  # Amélioration propriétaire

def mpl_violation():
    """Violation des conditions MPL"""
    # Violation: Modification MPL sans redistribution sous MPL
    enhanced = mpl_component.enhance(proprietary_enhancement)
    return enhanced  # Doit être sous licence MPL

# Vulnérabilité 5: Utilisation de code BSD avec suppression de copyright
# BSD nécessite la conservation de la notice de copyright
import bsd_library  # BSD 3-Clause - Copyright doit être conservé
import commercial_app  # Application commerciale

def bsd_violation():
    """Violation des conditions BSD"""
    # Violation: Suppression de la notice de copyright BSD
    stripped_code = bsd_library.remove_copyright()
    return commercial_app.use(stripped_code)

# Vulnérabilité 6: Utilisation de code MIT sans attribution
# MIT nécessite la conservation de la notice de copyright et de licence
import mit_library  # MIT License - Attribution requise
import internal_tool  # Outil interne

def mit_violation():
    """Violation des conditions MIT"""
    # Violation: Pas d'attribution MIT
    used_code = mit_library.function()
    return internal_tool.process(used_code)  # Pas d'attribution

# Vulnérabilité 7: Utilisation de code Apache 2.0 sans NOTICE
# Apache 2.0 nécessite la conservation du fichier NOTICE
import apache_library  # Apache 2.0 - NOTICE doit être conservé
import enterprise_app  # Application d'entreprise

def apache_violation():
    """Violation des conditions Apache 2.0"""
    # Violation: Suppression du fichier NOTICE Apache
    code_without_notice = apache_library.remove_notice()
    return enterprise_app.deploy(code_without_notice)

# Vulnérabilité 8: Utilisation de code propriétaire sans licence
# Code propriétaire nécessite une licence d'utilisation
import proprietary_sdk  # SDK propriétaire sans licence
import startup_app  # Application startup

def proprietary_violation():
    """Violation: Utilisation de code propriétaire sans licence"""
    # Violation: Utilisation sans licence
    result = proprietary_sdk.process()
    return startup_app.use(result)

# Vulnérabilité 9: Utilisation de code commercial dans un projet open source
# Code commercial ne peut pas être utilisé dans un projet open source
import commercial_library  # Bibliothèque commerciale
import open_source_project  # Projet open source

def commercial_in_opensource():
    """Violation: Code commercial dans projet open source"""
    # Violation: Code commercial dans open source
    commercial_result = commercial_library.function()
    return open_source_project.integrate(commercial_result)

# Vulnérabilité 10: Utilisation de code avec licence expirée
# Licence expirée ne permet plus l'utilisation
import expired_license_lib  # Bibliothèque avec licence expirée
import current_project  # Projet actuel

def expired_license_violation():
    """Violation: Utilisation de code avec licence expirée"""
    # Violation: Licence expirée
    result = expired_license_lib.function()
    return current_project.use(result)

# Vulnérabilité 11: Utilisation de code avec licence restrictive
# Licence restrictive limite l'usage commercial
import restrictive_library  # Licence restrictive
import commercial_product  # Produit commercial

def restrictive_license_violation():
    """Violation: Utilisation commerciale de licence restrictive"""
    # Violation: Usage commercial de licence restrictive
    result = restrictive_library.function()
    return commercial_product.sell(result)

# Vulnérabilité 12: Utilisation de code avec licence non-commerciale
# Licence non-commerciale interdit l'usage commercial
import noncommercial_lib  # Licence non-commerciale
import business_app  # Application commerciale

def noncommercial_violation():
    """Violation: Usage commercial de licence non-commerciale"""
    # Violation: Usage commercial de licence non-commerciale
    result = noncommercial_lib.function()
    return business_app.profit_from(result)

# Vulnérabilité 13: Utilisation de code avec licence académique
# Licence académique limite l'usage à des fins académiques
import academic_library  # Licence académique
import commercial_research  # Recherche commerciale

def academic_license_violation():
    """Violation: Usage commercial de licence académique"""
    # Violation: Usage commercial de licence académique
    result = academic_library.research()
    return commercial_research.use(result)

# Vulnérabilité 14: Utilisation de code avec licence personnelle
# Licence personnelle interdit l'usage professionnel
import personal_library  # Licence personnelle
import corporate_app  # Application d'entreprise

def personal_license_violation():
    """Violation: Usage professionnel de licence personnelle"""
    # Violation: Usage professionnel de licence personnelle
    result = personal_library.function()
    return corporate_app.use(result)

# Vulnérabilité 15: Utilisation de code avec licence d'évaluation
# Licence d'évaluation limite l'usage dans le temps
import evaluation_library  # Licence d'évaluation
import production_app  # Application en production

def evaluation_license_violation():
    """Violation: Usage en production de licence d'évaluation"""
    # Violation: Usage en production de licence d'évaluation
    result = evaluation_library.function()
    return production_app.deploy(result)

# Vulnérabilité 16: Utilisation de code avec licence de développement
# Licence de développement interdit l'usage en production
import dev_license_lib  # Licence de développement
import production_system  # Système en production

def dev_license_violation():
    """Violation: Usage en production de licence de développement"""
    # Violation: Usage en production de licence de développement
    result = dev_license_lib.function()
    return production_system.use(result)

# Vulnérabilité 17: Utilisation de code avec licence de test
# Licence de test interdit l'usage commercial
import test_license_lib  # Licence de test
import commercial_service  # Service commercial

def test_license_violation():
    """Violation: Usage commercial de licence de test"""
    # Violation: Usage commercial de licence de test
    result = test_license_lib.function()
    return commercial_service.offer(result)

# Vulnérabilité 18: Utilisation de code avec licence de démonstration
# Licence de démonstration interdit l'usage réel
import demo_license_lib  # Licence de démonstration
import real_application  # Application réelle

def demo_license_violation():
    """Violation: Usage réel de licence de démonstration"""
    # Violation: Usage réel de licence de démonstration
    result = demo_license_lib.function()
    return real_application.use(result)

# Vulnérabilité 19: Utilisation de code avec licence de recherche
# Licence de recherche interdit l'usage commercial
import research_library  # Licence de recherche
import commercial_product  # Produit commercial

def research_license_violation():
    """Violation: Usage commercial de licence de recherche"""
    # Violation: Usage commercial de licence de recherche
    result = research_library.function()
    return commercial_product.integrate(result)

# Vulnérabilité 20: Utilisation de code avec licence éducative
# Licence éducative interdit l'usage commercial
import educational_library  # Licence éducative
import commercial_platform  # Plateforme commerciale

def educational_license_violation():
    """Violation: Usage commercial de licence éducative"""
    # Violation: Usage commercial de licence éducative
    result = educational_library.function()
    return commercial_platform.use(result)

# Vulnérabilité 21: Utilisation de code avec licence gouvernementale
# Licence gouvernementale limite l'usage aux entités gouvernementales
import government_library  # Licence gouvernementale
import private_company  # Entreprise privée

def government_license_violation():
    """Violation: Usage privé de licence gouvernementale"""
    # Violation: Usage privé de licence gouvernementale
    result = government_library.function()
    return private_company.use(result)

# Vulnérabilité 22: Utilisation de code avec licence militaire
# Licence militaire limite l'usage aux applications militaires
import military_library  # Licence militaire
import civilian_app  # Application civile

def military_license_violation():
    """Violation: Usage civil de licence militaire"""
    # Violation: Usage civil de licence militaire
    result = military_library.function()
    return civilian_app.use(result)

# Vulnérabilité 23: Utilisation de code avec licence médicale
# Licence médicale limite l'usage aux applications médicales
import medical_library  # Licence médicale
import general_app  # Application générale

def medical_license_violation():
    """Violation: Usage général de licence médicale"""
    # Violation: Usage général de licence médicale
    result = medical_library.function()
    return general_app.use(result)

# Vulnérabilité 24: Utilisation de code avec licence financière
# Licence financière limite l'usage aux applications financières
import financial_library  # Licence financière
import non_financial_app  # Application non-financière

def financial_license_violation():
    """Violation: Usage non-financier de licence financière"""
    # Violation: Usage non-financier de licence financière
    result = financial_library.function()
    return non_financial_app.use(result)

# Vulnérabilité 25: Utilisation de code avec licence de sécurité
# Licence de sécurité limite l'usage aux applications de sécurité
import security_library  # Licence de sécurité
import general_security_app  # Application de sécurité générale

def security_license_violation():
    """Violation: Usage général de licence de sécurité"""
    # Violation: Usage général de licence de sécurité
    result = security_library.function()
    return general_security_app.use(result)

# Vulnérabilité 26: Utilisation de code avec licence de cryptographie
# Licence de cryptographie peut avoir des restrictions d'export
import crypto_library  # Licence de cryptographie
import international_app  # Application internationale

def crypto_license_violation():
    """Violation: Export de code cryptographique"""
    # Violation: Export de code cryptographique
    result = crypto_library.function()
    return international_app.export(result)

# Vulnérabilité 27: Utilisation de code avec licence de brevet
# Licence de brevet peut avoir des restrictions d'usage
import patent_licensed_lib  # Code sous licence de brevet
import unlicensed_app  # Application sans licence de brevet

def patent_license_violation():
    """Violation: Usage sans licence de brevet"""
    # Violation: Usage sans licence de brevet
    result = patent_licensed_lib.function()
    return unlicensed_app.use(result)

# Vulnérabilité 28: Utilisation de code avec licence de marque
# Licence de marque peut avoir des restrictions d'usage
import trademark_licensed_lib  # Code sous licence de marque
import unauthorized_app  # Application non autorisée

def trademark_license_violation():
    """Violation: Usage non autorisé de marque"""
    # Violation: Usage non autorisé de marque
    result = trademark_licensed_lib.function()
    return unauthorized_app.use(result)

# Vulnérabilité 29: Utilisation de code avec licence de secret commercial
# Licence de secret commercial interdit la divulgation
import trade_secret_lib  # Code sous licence de secret commercial
import public_app  # Application publique

def trade_secret_violation():
    """Violation: Divulgation de secret commercial"""
    # Violation: Divulgation de secret commercial
    result = trade_secret_lib.function()
    return public_app.disclose(result)

# Vulnérabilité 30: Utilisation de code avec licence de données personnelles
# Licence de données personnelles a des restrictions de protection
import personal_data_lib  # Code sous licence de données personnelles
import non_compliant_app  # Application non conforme RGPD

def personal_data_license_violation():
    """Violation: Usage non conforme de données personnelles"""
    # Violation: Usage non conforme de données personnelles
    result = personal_data_lib.function()
    return non_compliant_app.process(result)

# Vulnérabilités de licences incluses dans ce fichier:
# 1. GPL v3 dans projet propriétaire (copyleft fort)
# 2. AGPL dans application SaaS (copyleft réseau)
# 3. LGPL sans respect des conditions (copyleft faible)
# 4. MPL sans redistribution des modifications
# 5. BSD avec suppression de copyright
# 6. MIT sans attribution
# 7. Apache 2.0 sans NOTICE
# 8. Code propriétaire sans licence
# 9. Code commercial dans projet open source
# 10. Code avec licence expirée
# 11. Licence restrictive dans usage commercial
# 12. Licence non-commerciale dans usage commercial
# 13. Licence académique dans usage commercial
# 14. Licence personnelle dans usage professionnel
# 15. Licence d'évaluation en production
# 16. Licence de développement en production
# 17. Licence de test dans usage commercial
# 18. Licence de démonstration dans usage réel
# 19. Licence de recherche dans usage commercial
# 20. Licence éducative dans usage commercial
# 21. Licence gouvernementale dans usage privé
# 22. Licence militaire dans usage civil
# 23. Licence médicale dans usage général
# 24. Licence financière dans usage non-financier
# 25. Licence de sécurité dans usage général
# 26. Licence de cryptographie avec export non autorisé
# 27. Code sous brevet sans licence
# 28. Code sous marque sans autorisation
# 29. Secret commercial divulgué
# 30. Données personnelles non conformes RGPD 
